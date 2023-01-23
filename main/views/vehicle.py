from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404, get_object_or_404, render
from main.forms import VehicleUpdateForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
)
from main.models.vehicles import Vehicles
from main.models.logs import DataLogs
from main.models.devices import TrackingDevices
from django.contrib.auth.mixins import LoginRequiredMixin


class VehiclesListView(LoginRequiredMixin, ListView):
    login_required = True
    template_name = "main/vehicle/vehicle_list.html"
    model = Vehicles


class VehiclesDetailView(LoginRequiredMixin, View):
    template_name = "main/vehicle/vehicle_details.html"

    def get(self, request, pk):
        vehicle = get_object_or_404(Vehicles, pk=pk)
        try:
            logs = get_list_or_404(DataLogs, vehicle_id=vehicle.vehicle_id)[::-1]
        except:
            logs = None
        try:
            device = get_object_or_404(
                TrackingDevices, vehicle_id=vehicle.vehicle_id, active_device=True
            )
        except:
            device = None

        return render(
            request,
            template_name=self.template_name,
            context={"logs": logs, "vehicle": vehicle, "device": device},
        )


class VehicleCreateView(LoginRequiredMixin, CreateView):
    template_name = "main/vehicle/vehicle_create.html"
    model = Vehicles
    fields = [
        "vehicle_id",
        "vehicle_type_id",
        "vehicle_desc",
        "dt_bought",
        "dt_sold",
        "active_vehicle",
    ]
    success_url = reverse_lazy("vehicle_list")


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "main/vehicle/vehicle_update.html"
    model = Vehicles
    fields = [
        "vehicle_id",
        "vehicle_type_id",
        "vehicle_desc",
        "dt_bought",
        "dt_sold",
        "active_vehicle",
    ]
    success_url = reverse_lazy("vehicle_list")


# class VehicleUpdateViewa(LoginRequiredMixin, View):
#     template_name = "main/vehicle/vehicle_update.html"
#


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "main/vehicle/vehicle_delete.html"
    model = Vehicles
    success_url = reverse_lazy("vehicle_list")
