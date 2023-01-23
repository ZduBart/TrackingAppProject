from django import forms
from main.models.vehicles import Vehicles


class VehicleUpdateForm(forms.Form):
    model = Vehicles
    vehicle_id = forms.CharField(max_length=50)
