from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class loginform(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class signupform(UserCreationForm):
        firstname = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
        lastname = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
        username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
        password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
        confirmpassword = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
        email = forms.TimeField(
        widget= forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )
        address = forms.TimeField(
        widget= forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class Meta:
    model = User
    fields = ('username','email','password','confirmpassword','address','is_patient','is_doctor')
