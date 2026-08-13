from django import forms
from .models import HealthCenter


class HealthCenterForm(forms.ModelForm):
    class Meta:
        model = HealthCenter
        fields = ['name', 'type_centre', 'adresse', 'ville', 'telephone', 'est_ouvert', 'horaires']