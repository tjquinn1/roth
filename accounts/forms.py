from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from . import models
from .models import User

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("email", "password1", "password2", "first_name", "last_name")
        model = get_user_model()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields["first_name"].widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name'})
        self.fields["last_name"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields["password1"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields["password2"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Reenter Password'})
        

class CustomLoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields["password"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})

class PartialUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [

        ]