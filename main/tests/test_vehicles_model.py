from django.test import TestCase
from main.models.vehicles import Vehicles, VehicleTypes


class VehicleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        vehicle_type = VehicleTypes.objects.create(
            vehicle_type_id=1, vehicle_type_desc="Test type"
        )
        Vehicles.objects.create(
            vehicle_id=1,
            vehicle_type_id=vehicle_type,
            vehicle_desc="Pojazd testowy",
            dt_bought="2023-01-17",
            active_vehicle=True,
        )

    def test_vehicle_id_label(self):
        vehicle = Vehicles.objects.get(vehicle_id=1)
        field_label = vehicle._meta.get_field("vehicle_id").verbose_name
        self.assertEqual(field_label, "vehicle id")

    def test_vehicle_desc_length(self):
        vehicle = Vehicles.objects.get(vehicle_id=1)
        max_length = vehicle._meta.get_field("vehicle_desc").max_length
        self.assertEqual(max_length, 50)
