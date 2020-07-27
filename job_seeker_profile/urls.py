from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('cv/', CreateCV.as_view(), name='cv')
]
