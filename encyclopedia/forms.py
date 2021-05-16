
from django import forms
from .models import Items
from django.db import  models

class CreateNewPage(forms.Form):
    Model=Items
    title = forms.CharField(label="Title", max_length=200, widget=forms.TextInput(attrs={'class':'form-control-sm'}))
    description = forms.CharField(
        label='Description', max_length=1000,
        widget=forms.TextInput(attrs={'class':'form-control-lg'}))

class EditPage(forms.Form):
    model=Items
    template_name='edit.html'
    fields=['title','description']