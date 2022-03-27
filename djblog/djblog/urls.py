from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
# import django.contrib.auth.urls as secureurls
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', include('appblog.urls')),
    path('admin/', include('appadmin.urls'))

] #+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)