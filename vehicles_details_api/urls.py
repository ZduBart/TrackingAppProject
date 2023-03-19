from django.urls import path
from main.views.home import Home
from .views import GetVehicleDetailsByDay


urlpatterns = [
    path(
        "vehicles/<int:pk>/details/",
        GetVehicleDetailsByDay.as_view(),
        name="vehicle_details_api",
    ),
]
