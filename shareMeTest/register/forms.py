from typing import Any
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget= forms.TextInput
                           (attrs={'class':'username-field register-field'}), label="Username")
    email = forms.EmailField(widget= forms.EmailInput
                           (attrs={'class':'email-field register-field'}), label="Email")
    password1 = forms.CharField(widget= forms.PasswordInput
                           (attrs={'class':'password1-field register-field'}), label="Password")
    password2 = forms.CharField(widget= forms.PasswordInput
                           (attrs={'class':'password2-field register-field'}), label=" Password")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget= forms.TextInput
                           (attrs={'class':'username-field login-field'}), label="Username")
    password = forms.CharField(widget= forms.PasswordInput
                           (attrs={'class':'password-field login-field'}), label="Password")
    
    class Meta:
        model = User
        fields = ["username", "password"]