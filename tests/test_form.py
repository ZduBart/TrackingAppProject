from django.test import TestCase, Client
from main.forms import VehicleCreateForm, VehicleUpdateForm


class VehicleCreateFormTest(TestCase):
    def test_vehicle_empty_form(self):
        form = VehicleCreateForm()
        self.assertFormError(
            form=form,
        )

    def test_vehicle_id_not_integer(self):
        form = VehicleCreateForm(data={"vehicle_id": "xxx"})

        self.assertEqual(form.errors["vehicle_id"], ["“xxx” value must be an integer."])

    def test_vehicle_type_id_not_integer(self):
        form = VehicleCreateForm(data={"vehicle_type_id": "xxx"})

        self.assertEqual(
            form.errors["vehicle_type_id"],
            ["Select a valid choice. That choice is not one of the available choices."],
        )

    def test_vehicle_desc_too_long(self):
        form = VehicleCreateForm(data={"vehicle_desc": "aaa"})

        self.assertEqual(
            form.errors["vehicle_desc"],
            ["Select a valid choice. That choice is not one of the available choices."],
        )
