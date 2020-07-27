from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
# from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import (UserAccount, models)
from .forms import RegisterForm
from .models import UserAccount
from django.forms import ValidationError


def usersignup(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})
