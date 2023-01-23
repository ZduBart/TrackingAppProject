from django.db import models
from main.models.vehicles import Vehicles
from main.models.parameters import Parameters


class TrackingDevices(models.Model):
    device_id = models.IntegerField(primary_key=True)
    device_desc = models.TextField(max_length=50)
    vehicle_id = models.ForeignKey(
        Vehicles, db_column="vehicle_id", on_delete=models.CASCADE
    )
    dt_start = models.DateTimeField()
    dt_end = models.DateTimeField(blank=True, null=True)
    active_device = models.BooleanField()

    def __str__(self):
        return f"ID:{self.device_id} | {self.device_desc}"


class DeviceParam(models.Model):
    param_id = models.ForeignKey(
        Parameters, db_column="param_id", on_delete=models.CASCADE
    )
    device_id = models.ForeignKey(
        TrackingDevices, db_column="device_id", on_delete=models.CASCADE
    )
    active = models.BooleanField()

    def __str__(self):
        return f"ID param :{self.param_id} | ID device {self.device_id}"
