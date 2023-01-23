from django.contrib import admin
from main.models.devices import TrackingDevices, DeviceParam
from main.models.parameters import Parameters
from main.models.vehicles import Vehicles, VehicleTypes
from main.models.logs import DataLogs


admin.site.register(
    [TrackingDevices, DeviceParam, Parameters, Vehicles, VehicleTypes, DataLogs]
)
