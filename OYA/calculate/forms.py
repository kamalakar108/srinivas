from django import forms
from calculate.models import maths
class mathsForm(forms.ModelForm):
    class Meta:
        model=maths
        fields='__all__'
