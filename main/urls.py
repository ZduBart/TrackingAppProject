from django.urls import path
from main.views.home import Home
from main.views.vehicle import (
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
    DevicesCreateView,
)
from main.views.parameters import (
    ParametersListView,
    ParametersDeleteView,
    ParametersUpdateView,
    ParametersDetailView,
    ParametersCreateView,
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
    path("devices/create", DevicesCreateView.as_view(), name="device_create"),
    path("devices/delete/<int:pk>", DevicesDeleteView.as_view(), name="device_delete"),
    path("devices/update/<int:pk>", DevicesUpdateView.as_view(), name="device_update"),
    path("devices/<int:pk>", DevicesDetailView.as_view(), name="device_detail"),
    path("parameters", ParametersListView.as_view(), name="parameter_list"),
    path("parameters/create", ParametersCreateView.as_view(), name="parameter_create"),
    path(
        "parameters/delete/<int:pk>",
        ParametersDeleteView.as_view(),
        name="parameter_delete",
    ),
    path(
        "parameters/update/<int:pk>",
        ParametersUpdateView.as_view(),
        name="parameter_update",
    ),
    path(
        "parameters/<int:pk>", ParametersDetailView.as_view(), name="parameter_detail"
    ),
    path("", Home.as_view(), name="home"),
]
