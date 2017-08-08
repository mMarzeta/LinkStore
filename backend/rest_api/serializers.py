from rest_framework import serializers
from .models import Category, Link


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description')


class LinkSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Link
        fields = ('id', 'url', 'category', 'description')