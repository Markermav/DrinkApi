from unicodedata import name
from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()


    def __str__(self) -> str:
        return self.name


class ColdDrinks(models.Model):
    name = models.CharField(max_length=100)
    flavour = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name
     

class Food(models.Model):
    name = models.CharField(max_length=255)
    description =  models.CharField(max_length=255)
    region = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name


