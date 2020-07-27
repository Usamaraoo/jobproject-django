# from django import forms
# from django.contrib.auth.models import User
#
# from .models import UserAccount
#
#
# class UserSignupForm(forms.ModelForm):
#     class Meta:
#         model = UserAccount
#         fields = ['first_name', 'last_name', 'username', 'email', 'password',
#                   'gender', 'contact_number', 'email_notifi_active', 'user_image']
#
#     def emial_check(self):
#         e = self.cleaned_data['email']
#         email = User.objects.get(email=e)
#         if email != '':
#             raise forms.ValidationError("Email address already Exists")
#         return email
#
#
# class UserLogin(forms.Form):
#     email = forms.EmailField()
#     Password = forms.CharField(max_length=40)
#
#     def emial_check(self):
#         e = self.cleaned_data['email']
#         email = UserAccount.objects.get(email=e)
#         if email == '':
#             raise forms.Validationrror("Email address not Exists")
#         return email

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
