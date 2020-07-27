from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('', home),  # this is main page
    path('admin/', admin.site.urls),
    path('job_post_management/', include('job_post_management.urls')),
    path('job_seeker_profile/', include('job_seeker_profile.urls')),
    path('user_management/', include('user_management.urls')),
    path('CompanyProfile/', include('CompanyProfile.urls')),
    # for login
    path('', include("django.contrib.auth.urls"))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
