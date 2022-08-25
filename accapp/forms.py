from dataclasses import field
from itertools import product
from django import forms
from accapp.models import *

class product_Form(forms.ModelForm):
    class Meta:
        model=product
        fields=('name','price','description','image')


class reachus_Form(forms.ModelForm):
    class Meta:
        model=reachus
        fields='__all__'