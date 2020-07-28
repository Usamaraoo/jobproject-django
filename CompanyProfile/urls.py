from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', company_signup, name='register-company'),
    path('company/login/', company_login, name='login-company'),
]
