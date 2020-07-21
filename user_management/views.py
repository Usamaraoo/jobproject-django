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
from .forms import (UserSignupForm, UserLogin)
from .models import UserAccount
from django.forms import ValidationError
def usersignup(request):
    form = UserSignupForm

    if request.method == 'POST':
        form = UserSignupForm(request.POST ,request.FILES or None)

        if form.is_valid():
            form.save()
            from django.contrib import messages
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('/')
        else:
            ValidationError('Error')
    else:
        forms = UserSignupForm()
    context = {'forms': form}
    return render(request, 'user_management/forms.html',context )


def user_login(request):
    forms = UserLogin
    if request.method == 'POST':
        forms = UserLogin(request.POST)
        if forms.is_valid():
            return HttpResponse("loggedin")

    context = {'forms': forms}
    return render(request, 'Home.html', context)
