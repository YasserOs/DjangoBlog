from django.contrib import admin
from django.urls import path,include
# import django.contrib.auth.urls as secureurls
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appblog.urls')),
#     path('members/', include('members.urls')),
#     path('members/', include(secureurls)),

] # + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)