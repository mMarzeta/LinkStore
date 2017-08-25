from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from django.http import JsonResponse

from rest_api.serializers import LinkSerializer, CategorySerializer
from rest_api.models import Link, Category


@api_view(['GET'])
def index_page_view(request):
    if request.method == 'GET':
        data = {
            'content': 'index'
        }
        return JsonResponse(data)


#############
#   LINKS   #
#############

@api_view(['POST'])
def add_link(request):
    if request.method == 'POST':
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# get, put
def link_details(request, pk):
    if request.method == 'GET':
        links = Link.objects.all()
        link_serializer = LinkSerializer(links, many=True)
        return JsonResponse(link_serializer)


################
#   Category   #
################

@api_view(['POST'])
def add_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# post, put
def category_details(request, pk):
    data = {
        'content': 'category details'
    }
    return JsonResponse(data)


def link_list():
    pass


def category_list():
    pass
