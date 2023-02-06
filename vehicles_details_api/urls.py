from django.urls import path
from main.views.home import Home
from .views import GetVehicleDetailsByDay


urlpatterns = [
    path(
        "vehicles/<int:pk>/day/", GetVehicleDetailsByDay.as_view(), name="vehicle_list"
    ),
]
