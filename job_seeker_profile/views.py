from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import CreateView
from .models import CV


def index(request):
    return HttpResponse("Helow form job_seeker_profile")


class CreateCV(CreateView):
    model = CV
    template_name = 'job_seeker_profile/cv.html'
    fields = '__all__'
