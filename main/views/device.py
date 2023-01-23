from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls import reverse_lazy
from main.models.vehicles import Vehicles
from main.models.devices import TrackingDevices


class DevicesListView(LoginRequiredMixin, ListView):
    login_required = True
    template_name = "main/device_list.html"
    model = TrackingDevices


class DevicesDetailView(LoginRequiredMixin, View):
    template_name = "main/device_detail.html"

    def get(self, request, pk):
        device = get_object_or_404(TrackingDevices, pk=pk)
        vehicle = Vehicles.objects.get(
            vehicle_id=device.vehicle_id_id
        )  # czemu taki zapis?
        vehicle = device.vehicle_id

        return render(
            request,
            template_name=self.template_name,
            context={"device": device, "vehicle": vehicle},
        )


class DevicesDeleteView(LoginRequiredMixin, DeleteView):
    model = TrackingDevices
    template_name = "main/device_delete.html"
    success_url = reverse_lazy("device_list")


class DevicesUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "main/device_update.html"
    model = TrackingDevices
    fields = [
        "device_id",
        "device_desc",
        "vehicle_id",
        "dt_start",
        "dt_end",
        "active_device",
    ]
    success_url = reverse_lazy("device_list")
