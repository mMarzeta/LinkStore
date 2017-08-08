from django.shortcuts import render
from django.http import JsonResponse


#get
def index_page_view(request):
    data = {
        'content': 'main_page',
    }
    return JsonResponse(data)


#psot
def add_link(request):
    data = {
        'content': 'post tutaj',
    }
    return JsonResponse(data)

#get, put
def link_details(request, pk):
    data = {
        'content': 'link_details'
    }
    return JsonResponse(data)

#post
def add_category(request):
    data = {
        'content': 'add_category'
    }
    return JsonResponse(data)

#post, put
def category_details(request, pk):
    data = {
        'content': 'category details'
    }
    return JsonResponse(data)