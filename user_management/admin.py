from django.contrib import admin
from .models import (UserLog,UserAccount,)

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(UserLog)
