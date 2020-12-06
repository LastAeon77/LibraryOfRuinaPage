from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# A simple form for user registration, uses Django's template
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
