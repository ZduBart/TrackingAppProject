from django.db import models
from django.urls import reverse


class DataLogs(models.Model):
    id = models.IntegerField(primary_key=True)
    device_id = models.ForeignKey(
        TrackingDevices, db_column="device_id", on_delete=models.CASCADE
    )
    vehicle_id = models.ForeignKey(
        Vehicles, db_column="vehicle_id", on_delete=models.CASCADE
    )
    dt_log = models.DateTimeField()
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)
    engine_rpm = models.IntegerField()
    engine_on = models.BooleanField()
    coolant_temp = models.IntegerField()
    oil_temp = models.IntegerField()
    active_log = models.BooleanField()

    def __str__(self):
        return f"ID:{self.id} | {self.dt_log}"
