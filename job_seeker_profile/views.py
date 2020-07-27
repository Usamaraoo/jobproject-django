from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import generic
from .models import CV


def index(request):
    return HttpResponse("Helow form job_seeker_profile")


class CreateCV(generic.CreateView):
    model = CV
    template_name = 'job_seeker_profile/createcv.html'
    fields = '__all__'
    context_object_name = 'cv'


class CvViewer(generic.DetailView):
    model = CV
    template_name = 'job_seeker_profile/cv.html'
    context_object_name = 'cv'


class CvUpdate(generic.UpdateView):
    model = CV
    template_name = 'job_seeker_profile/createcv.html'
    fields = '__all__'
    context_object_name = 'cv'
