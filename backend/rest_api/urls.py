from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', index_page_view),
    url(r'add-link/$', add_link),
    url(r'link/(?P<pk>[0-9]+)$', link_details),
    url(r'add-category/$', add_category),
    url(r'category/(?P<pk>[0-9]+)$', category_details),
    url(r'links-list', link_list),
    url(r'categories-list', category_list)
]
