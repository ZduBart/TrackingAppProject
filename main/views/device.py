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
from main.models.devices import TrackingDevices, DeviceParam
from main.models.parameters import Parameters


class DevicesListView(LoginRequiredMixin, ListView):
    template_name = "main/device/device_list.html"
    model = TrackingDevices


class DevicesDetailView(LoginRequiredMixin, View):
    template_name = "main/device/device_detail.html"

    def get(self, request, pk):
        device = get_object_or_404(TrackingDevices, pk=pk)
        try:
            vehicle = get_object_or_404(
                Vehicles, vehicle_id=device.vehicle_id.vehicle_id
            )
        except:
            vehicle = None
        try:
            parameters = get_list_or_404(DeviceParam, device_id=device.device_id)
        except:
            parameters = None

        return render(
            request,
            template_name=self.template_name,
            context={"device": device, "vehicle": vehicle, "params": parameters},
        )


class DevicesDeleteView(LoginRequiredMixin, DeleteView):
    model = TrackingDevices
    template_name = "main/device/device_delete.html"
    success_url = reverse_lazy("device_list")


class DevicesUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "main/device/device_update.html"
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


class DevicesCreateView(LoginRequiredMixin, CreateView):
    template_name = "main/device/device_create.html"
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
