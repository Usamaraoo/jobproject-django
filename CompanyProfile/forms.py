from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Company
class CompanyRegistrationForm(UserCreationForm):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyLogin(forms.Form):
    login = forms.EmailField()
    Password = forms.CharField(max_length=40)
