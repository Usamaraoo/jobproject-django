from django import forms
from .models import Company
class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyLogin(forms.Form):
    login = forms.EmailField()
    Password = forms.CharField(max_length=40)
