from django.contrib import admin
from .models import (EducationDetail, CV, SkillSet, ExperienceDetail,
                     SeekerSkillSet, Location, PDF, Reference, )

# Register your models here.
admin.site.register(EducationDetail)
admin.site.register(CV)
admin.site.register(SkillSet)
admin.site.register(ExperienceDetail)
admin.site.register(SeekerSkillSet)
admin.site.register(Location)
admin.site.register(PDF)
admin.site.register(Reference)
