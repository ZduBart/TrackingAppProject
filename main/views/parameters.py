from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)

from main.models.devices import DeviceParam, TrackingDevices
from main.models.parameters import Parameters


class ParametersListView(LoginRequiredMixin, ListView):
    template_name = "main/parameter/parameter_list.html"
    model = Parameters


class ParametersDetailView(LoginRequiredMixin, View):
    template_name = "main/parameter/parameter_details.html"

    def get(self, request, pk):
        parameter = get_object_or_404(Parameters, pk=pk)
        try:
            devices = get_list_or_404(DeviceParam, param_id=parameter.param_id)
        except DeviceParam.DoesNotExist:
            devices = None

        return render(
            request,
            template_name=self.template_name,
            context={"param": parameter, "devices": devices},
        )


class ParametersDeleteView(LoginRequiredMixin, DeleteView):
    model = Parameters
    template_name = "main/parameter/parameter_delete.html"
    success_url = reverse_lazy("parameter_list")


class ParametersUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "main/parameter/parameter_update.html"
    model = Parameters
    fields = [
        "param_id",
        "param_desc",
    ]
    success_url = reverse_lazy("parameter_list")


class ParametersCreateView(LoginRequiredMixin, CreateView):
    template_name = "main/parameter/parameter_create.html"
    model = Parameters
    fields = ["param_id", "param_desc"]
    success_url = reverse_lazy("parameter_list")
