from django.urls import reverse_lazy
from django.shortcuts import render
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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class VehiclesListView(LoginRequiredMixin, ListView):
    template_name = "main/vehicle/vehicle_list.html"
    model = Vehicles

    def get_queryset(self):
        vehicle_search = self.request.GET.get("name", "").lower()
        vehicles = self.model.objects.all()
        if len(vehicle_search) > 0:
            vehicles = vehicles.filter(vehicle_desc__icontains=vehicle_search)
        return vehicles


class VehiclesDetailView(LoginRequiredMixin, View):
    template_name = "main/vehicle/vehicle_details.html"

    def get(self, request, pk):

        page_num = request.GET.get("page", 1)

        try:
            vehicle = Vehicles.objects.get(pk=pk)
        except Vehicles.DoesNotExist:
            return render(
                request, template_name=self.template_name, context={"vehicle": None}
            )

        logs = DataLogs.objects.filter(vehicle_id=vehicle.vehicle_id).all()[::-1]
        device = TrackingDevices.objects.filter(
            vehicle_id=vehicle.vehicle_id, active_device=True
        ).first()

        paginator = Paginator(logs, 10)
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        return render(
            request,
            template_name=self.template_name,
            context={
                "logs_paginator": page_obj,
                "vehicle": vehicle,
                "device": device,
            },
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
