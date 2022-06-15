from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ColdDrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColdDrinks
        fields = ['id', 'name', 'flavour', 'price']

         
class FoodSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Food
       fields = ['id', 'url', 'name', 'description', 'region', 'price']


    