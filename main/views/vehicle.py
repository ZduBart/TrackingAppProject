from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    View,
)
from main.models.vehicles import Vehicles, VehicleTypes
from main.models.logs import DataLogs
from main.models.devices import TrackingDevices
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main.forms import VehicleUpdateForm, VehicleCreateForm


class VehiclesListView(LoginRequiredMixin, View):
    template_name = "main/vehicle/vehicle_list.html"

    def get(self, request):
        vehicle_search_query = self.request.GET.get("name", "").lower()
        vehicle_type_query = self.request.GET.get("type", "")
        vehicles = Vehicles.objects.all()
        vehicle_types = VehicleTypes.objects.all()

        if len(vehicle_search_query) > 0 and len(vehicle_type_query) > 0:
            vehicles = vehicles.filter(
                vehicle_desc__icontains=vehicle_search_query,
                vehicle_type_id__vehicle_type_id=vehicle_type_query,
            )
        elif len(vehicle_search_query) > 0:
            vehicles = vehicles.filter(vehicle_desc__icontains=vehicle_search_query)
        elif len(vehicle_type_query) > 0:
            vehicles = vehicles.filter(
                vehicle_type_id__vehicle_type_id=vehicle_type_query
            )

        return render(
            request,
            template_name=self.template_name,
            context={"vehicles": vehicles, "vehicle_types": vehicle_types},
        )


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
        if logs:
            paginator = Paginator(logs, 10)
            try:
                page_obj = paginator.page(page_num)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
        else:
            page_obj = None

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
    form_class = VehicleCreateForm
    success_url = reverse_lazy("vehicle_list")


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "main/vehicle/vehicle_update.html"
    model = Vehicles
    form_class = VehicleUpdateForm

    success_url = reverse_lazy("vehicle_list")


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "main/vehicle/vehicle_delete.html"
    model = Vehicles
    success_url = reverse_lazy("vehicle_list")
