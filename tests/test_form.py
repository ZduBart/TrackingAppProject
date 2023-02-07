from django.test import TestCase
from main.forms import VehicleCreateForm


class VehicleCreateFormTest(TestCase):
    def test_vehicle_id_not_integer(self):
        form = VehicleCreateForm(data={"vehicle_id": "xxx"})

        self.assertEqual(form.errors["vehicle_id"], ["“xxx” value must be an integer."])

    def test_vehicle_type_id_not_valid_type(self):
        form = VehicleCreateForm(data={"vehicle_type_id": "xxx"})

        self.assertEqual(
            form.errors["vehicle_type_id"],
            ["Select a valid choice. That choice is not one of the available choices."],
        )

    def test_vehicle_desc_too_long(self):
        form = VehicleCreateForm(data={"vehicle_desc": 51 * "a"})

        self.assertEqual(
            form.errors["vehicle_desc"],
            ["Ensure this value has at most 50 characters (it has 51)."],
        )
