from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    C_CARS = 'CARS'
    C_SHIPS = 'SHIPS'
    C_AIRPLANES = 'AIRPLANES'

    C_CHOICES = (
        (C_CARS, 'cars'),
        (C_SHIPS, 'ships'),
        (C_AIRPLANES, 'airplanes')
    )

    name = models.TextField(choices=C_CHOICES)


class ItemModel(models.Model):
    name = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
