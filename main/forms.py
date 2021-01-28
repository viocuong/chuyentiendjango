from django import forms
from .models import *
class AddForm(forms.ModelForm):
   
    class Meta:

        model = Bill
        fields = ['name','money','date','image']

