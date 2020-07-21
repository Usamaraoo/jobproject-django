from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
from .forms import (CompanyRegistrationForm, CompanyLogin)


def company_register(request):
    forms = CompanyRegistrationForm()
    return render(request, 'CompanyProfile/forms.html', {'forms': forms})


def company_login(request):
    forms = CompanyLogin()
    context = {'forms': forms}
    return render(request, 'Home.html', context)
