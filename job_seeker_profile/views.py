from django.shortcuts import render
from django.shortcuts import HttpResponse
def index(request):
    return HttpResponse("Helow form job_seeker_profile")