from django.conf.urls import url, include
from django.contrib import admin
from rest_api import views as rest_api_view
from rest_framework import routers


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^link-store/', include('rest_api.urls')),
]
