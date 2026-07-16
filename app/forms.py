from django import forms
from .models import Std


class StdForm(forms.ModelForm):
    class Meta:
        model=Std
        fields="__all__"

