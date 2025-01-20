from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'}),
    )
    avatar_img = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'Avatar URL'}),
    )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
    )


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'avatar_img', 'email', 'password1', 'password2']
