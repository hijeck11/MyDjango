from django import forms
from .models import Registration

class ItemForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ['event', 'attendee_name', 'attendee_email']

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()