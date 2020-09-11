from rest_framework import serializers
from exampleproject.exampleapp import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.CategoryModel


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.ItemModel
