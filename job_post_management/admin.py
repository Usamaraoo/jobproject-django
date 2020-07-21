from django.contrib import admin
from .models import (JobPostActivity,JobPostSkillSet,JobType,JobPost)
# Register your models here.
admin.site.register(JobPostSkillSet)
admin.site.register(JobPostActivity)
admin.site.register(JobType)
admin.site.register(JobPost)