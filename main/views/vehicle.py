from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from main.models.vehicles import Vehicles
from django.contrib.auth.mixins import LoginRequiredMixin


class VehiclesListView(LoginRequiredMixin, ListView):
    login_required = True
    template_name = "main/vehicle_list.html"
    model = Vehicles


class VehiclesDetailView(LoginRequiredMixin, DetailView):
    template_name = "main/vehicle_details.html"
    model = Vehicles


class VehicleCreateView(LoginRequiredMixin, CreateView):
    template_name = "main/vehicle_create.html"
    model = Vehicles
    fields = [
        "vehicle_id",
        "vehicle_type_id",
        "vehicle_desc",
        "dt_bought",
        "dt_sold",
        "active_vehicle",
    ]


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "main/vehicle_update.html"
    model = Vehicles
    fields = [
        "vehicle_id",
        "vehicle_type_id",
        "vehicle_desc",
        "dt_bought",
        "dt_sold",
        "active_vehicle",
    ]


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "main/vehicle_delete.html"
    model = Vehicles
    success_url = reverse_lazy("vehicle_list")
