from django.conf import settings
from django.urls import path
from uploader import views
from django.conf.urls.static import static

urlpatterns = [
    # Route for the main landing page
    path('', views.home_page, name='home'),
    
    # Route for the BMI Calculator page
    path('bmi/', views.bmi_page, name='bmi_calc'),
    
    # Route for the Image Uploader page
    path('upload/', views.upload_page, name='upload'),
]

# Serving media files during development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)