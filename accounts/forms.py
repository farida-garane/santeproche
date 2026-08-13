from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class InscriptionForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.Role.choices)
    telephone = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'telephone', 'password1', 'password2']
