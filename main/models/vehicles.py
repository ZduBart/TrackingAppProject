from django.db import models


class VehicleTypes(models.Model):
    vehicle_type_id = models.IntegerField(primary_key=True)
    vehicle_type_desc = models.TextField(max_length=50)

    def __str__(self):
        return f"ID:{self.vehicle_type_id} | {self.vehicle_type_desc}"


class Vehicles(models.Model):
    vehicle_id = models.IntegerField(primary_key=True)
    vehicle_type_id = models.ForeignKey(
        VehicleTypes, db_column="vehicle_type_id", on_delete=models.CASCADE
    )
    vehicle_desc = models.TextField(max_length=50)
    dt_bought = models.DateField()
    dt_sold = models.DateField(blank=True, null=True)
    active_vehicle = models.BooleanField()
