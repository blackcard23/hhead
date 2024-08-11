from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Polzovatel

class RegisterForm(UserCreationForm):
    class Meta:
        model = Polzovatel
        fields = ('username', 'rol', 'password1', 'password2')
