from django.urls import path
from main.views.home import home
from main.views.vehicle import (
    Vehicles,
    VehicleDeleteView,
    VehicleUpdateView,
    VehicleCreateView,
    VehiclesListView,
    VehiclesDetailView,
)
from main.views.device import (
    DevicesListView,
    DevicesDeleteView,
    DevicesDetailView,
    DevicesUpdateView,
)

urlpatterns = [
    path("vehicles/", VehiclesListView.as_view(), name="vehicle_list"),
    path("vehicles/<int:pk>/", VehiclesDetailView.as_view(), name="vehicle_detail"),
    path("vehicles/create/", VehicleCreateView.as_view(), name="vehicle_create"),
    path(
        "vehicles/update/<int:pk>", VehicleUpdateView.as_view(), name="vehicle_update"
    ),
    path(
        "vehicles/delete/<int:pk>", VehicleDeleteView.as_view(), name="vehicle_delete"
    ),
    path("devices", DevicesListView.as_view(), name="device_list"),
    path("devices/create", DevicesListView.as_view(), name="device_create"),
    path("devices/delete/<int:pk>", DevicesDeleteView.as_view(), name="device_delete"),
    path("devices/update/<int:pk>", DevicesUpdateView.as_view(), name="device_update"),
    path("devices/<int:pk>", DevicesDetailView.as_view(), name="device_detail"),
    path("", home, name="home"),
]
