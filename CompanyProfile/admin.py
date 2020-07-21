from django.contrib import admin
from .models import (CompanyLog, Company)
# Register your models here.
admin.site.register(Company)
admin.site.register(CompanyLog)