from django import forms
from .models import Ganhos


class GanhosForm(forms.ModelForm):
    class Meta:
        model = Ganhos
        fields = ['name', 'price']