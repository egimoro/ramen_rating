from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import RamenUser

class RamenUserCreationForm(UserCreationForm):

    class Meta:
        model = RamenUser
        fields = ['username', 'email']

class RamenUserChangeForm(UserChangeForm):

    class Meta:
        model = RamenUser
        fields = ['username', 'email']
