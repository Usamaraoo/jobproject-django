from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
from .forms import (CompanyRegistrationForm, CompanyLogin)
from django.views import generic
from django.shortcuts import redirect

def company_signup(request):
    form = CompanyRegistrationForm()
    # if request.method == 'POST':
    #     form = CompanyRegistrationForm(request.POST)
    #     if form.is_valid():
    #         forms.save()
    #         return redirect('/')
    # else:
    #     return CompanyRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def company_login(request):
    forms = CompanyLogin()
    context = {'forms': forms}
    return render(request, 'CompanyProfile/forms.html', context)


