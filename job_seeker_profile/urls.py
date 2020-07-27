from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('create_cv/', CreateCV.as_view(), name='createcv'),
    path('cv/<int:pk>', CvViewer.as_view(), name='cv'),
    path('cv_update/<int:pk>', CvUpdate.as_view(), name='cv_update'),
]
