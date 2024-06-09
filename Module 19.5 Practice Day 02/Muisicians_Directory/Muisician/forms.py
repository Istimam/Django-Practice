from django import forms
from .models import Muisician

class MuisicianForm(forms.ModelForm):
    class Meta:
        model = Muisician
        fields = '__all__'