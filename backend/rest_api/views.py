from django.shortcuts import render
from django.http import JsonResponse

def endpoint(request):
    data = {
        'text': 'zaczynamy',
        'status': 'konto napelnia sie',
    }
    return JsonResponse(data)