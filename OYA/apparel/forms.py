from django import forms
from apparel.models import PRODUCTS,CUSTOMERS,ORDERS
class PRODUCTSForm(forms.ModelForm):
    class Meta:
        model=PRODUCTS
        fields='__all__'

class CUSTOMERSForm(forms.ModelForm):
        class Meta:
            model=CUSTOMERS
            fields='__all__'

class ORDERSForm(forms.ModelForm):
        class Meta:
            model=ORDERS
            fields='__all__'
