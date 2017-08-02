from django.conf.urls import url, include
from django.contrib import admin
from rest_api import views as rest_api_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^link-store/', rest_api_view.endpoint),
]
