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


class SearchForm(forms.Form):
    airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        label="Select Airport"
    )
    direction = forms.ChoiceField(
        choices=(('L', 'Left'), ('R', 'Right')),
        label="Direction"
    )
