from django import forms
from .models import Airport


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = [
            'airport_name',
            'airport_code',
            'position',
            'duration',
            'left',
            'right'
        ]
