from django import forms
from django.contrib.auth.forms import UserCreationForm

from mailing.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class PasswordResetForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
