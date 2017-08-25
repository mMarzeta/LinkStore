from django.conf.urls import url, include
from .views import *

urlpatterns = [
    # spis moich linkow
    url(r'^$', index_page_view),
    url(r'add-link/$', add_link),
    # informacje o linku
    url(r'link/(?P<pk>[0-9]+)$', link_details),
    url(r'add-category/$', add_category),
    url(r'category/(?P<pk>[0-9]+)$', category_details),
]
