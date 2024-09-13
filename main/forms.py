from django import forms
from .models import American

class AmericanForm(forms.ModelForm):
    class Meta:
        model = American
        fields = ['name', 'rate' ]
