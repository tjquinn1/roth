from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms

class CourtCaseForm(forms.Form):
    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)