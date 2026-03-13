
from django.conf import settings
from django.urls import include, path
from uploader import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.upload_page, name='upload'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
