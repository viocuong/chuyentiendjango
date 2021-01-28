from django import forms
from .models import *
class AddForm(forms.ModelForm):
   
    class Meta:

        model = Bill
        fields = ['money','date','image']

