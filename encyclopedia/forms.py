from django import forms


class CreateNewPage(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    description = forms.CharField(label='Description', max_length=10000)
class EditPage(forms.Form):

    description = forms.CharField(label='Description', max_length=10000)