from django import forms
from .models import Airport


class AirportForm(forms.ModelForm):
    """
    Form for creating and updating Airport records.
    """
    class Meta:
        model = Airport
        fields = [
            'airport_name',
            'airport_code',
            'position',
            'duration',
            'left',
            'right',
        ]


class SearchForm(forms.Form):
    """
    Form used to select a starting airport and traversal direction
    for finding connected airport paths.
    """
    airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        empty_label="Select Airport"
    )

    direction = forms.ChoiceField(
        choices=(('L', 'Left'), ('R', 'Right')),
        widget=forms.RadioSelect
    )
