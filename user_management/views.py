from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserSignupForm
from .models import UserAccount
from django.forms import ValidationError


def usersignup(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['username']
            print('this is password ', a)
            form.save()

            return redirect("/")
    else:
        form = UserSignupForm()

    return render(request, "registration/register.html", {"form": form})
