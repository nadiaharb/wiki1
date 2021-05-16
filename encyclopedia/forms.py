
from django import forms
from django.forms import ModelForm

from .models import Items
from django.db import  models

class CreateNewPage(ModelForm):
    class Meta:
        model = Items
        fields='__all__'




class EditPage(forms.Form):
    model=Items
    template_name='edit.html'
    fields=['title','description']
    title = forms.CharField(label="Title", max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control-sm'}))
    description = forms.CharField(
        label='Description', max_length=1000,
        widget=forms.TextInput(attrs={'class': 'form-control-lg'}))
    edit = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required=False)