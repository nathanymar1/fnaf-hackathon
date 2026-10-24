from django import forms
from .models import MaintenanceRequest

class RequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ["building", "room", "email", "description"]