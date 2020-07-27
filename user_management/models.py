from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class UserAccount(User):
    Gender = [
        ('M', 'male'),
        ('F', 'female'),
    ]
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=2, choices=Gender, default='M')
    contact_number = models.CharField(max_length=20, blank=True, null=True, unique=True)
    email_notifi_active = models.BooleanField(blank=True)
    user_image = models.ImageField(blank=True, default='images/defaultuserimage.jpg')

    class MetaL:
        verbose_name = 'UserAccount'
        verbose_name_plural = 'UserAcounts'


# date and auto_add check out
# double password
class UserLog(models.Model):
    user_account_id = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
    last_login_date = models.DateTimeField(blank=True, null=True)
    last_jobapply_date = models.DateTimeField(blank=True, null=True)
