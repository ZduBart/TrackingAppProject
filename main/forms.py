from django import forms
from main.models.vehicles import Vehicles, VehicleTypes
from django.forms.widgets import NumberInput


class VehicleUpdateForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = [
            "vehicle_id",
            "vehicle_type_id",
            "vehicle_desc",
            "dt_bought",
            "dt_sold",
            "active_vehicle",
        ]

    vehicle_id = forms.CharField(max_length=50)
    vehicle_type_id = forms.ModelChoiceField(queryset=VehicleTypes.objects.all())
    vehicle_desc = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    dt_bought = forms.DateField(widget=NumberInput(attrs={"type": "date"}))
    dt_sold = forms.DateField(
        widget=NumberInput(attrs={"type": "date"}), required=False
    )
    active_vehicle = forms.BooleanField(required=False)


class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = [
            "vehicle_id",
            "vehicle_type_id",
            "vehicle_desc",
            "dt_bought",
            "active_vehicle",
        ]

    vehicle_id = forms.CharField(max_length=50)
    vehicle_type_id = forms.ModelChoiceField(queryset=VehicleTypes.objects.all())
    vehicle_desc = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    dt_bought = forms.DateField(widget=NumberInput(attrs={"type": "date"}))
    active_vehicle = forms.BooleanField(required=False)
