from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User

from .models import UserAccount


class UserSignupForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'username', 'email', 'password',
                  'gender', 'contact_number', 'email_notifi_active', 'user_image']
