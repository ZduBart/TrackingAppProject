from django.shortcuts import get_list_or_404, get_object_or_404, render
from main.models import Vehicles, TrackingDevices


device = get_object_or_404(TrackingDevices, pk=1)
vehicle = get_object_or_404(Vehicles, vehicle_id=device.vehicle_id)

print(device)
print(vehicle)
