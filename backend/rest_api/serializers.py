from rest_framework import serializers
from rest_api.models import Category, Link


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('pk', 'title', 'description')


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('url', 'category', 'description')
