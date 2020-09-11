from django.shortcuts import render
from exampleproject.exampleapp import models, serializers
from rest_framework import viewsets


class CategorySetView(viewsets.ModelViewSet):

    serializer_class = serializers.CategorySerializer
    queryset = models.CategoryModel.objects.all()
    filterset_fields = ('name',)


class ItemSetView(viewsets.ModelViewSet):

    serializer_class = serializers.ItemSerializer
    queryset = models.ItemModel.objects.all()
    filterset_fields = ('name', 'category')
