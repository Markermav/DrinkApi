from functools import partial
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view

from .models import *
from .serializers import *

from rest_framework import viewsets

# Create your views here.

class Food(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer




@api_view(['GET'])
def home(request):
    return Response({'message': 'Api Health good'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_records(request):
    p = Product.objects.all()
    serialize = ProductSerializer(p, many=True) 
    return Response(serialize.data, status=status.HTTP_200_OK)  

@api_view(['GET'])
def get_all_drinks(request):
    d = ColdDrinks.objects.all()
    serialize = ColdDrinksSerializer(d, many=True)
    return Response(serialize.data, status=status.HTTP_200_OK)  


@api_view(['POST'])
def createColdDrinks(request):
    serialize = ColdDrinksSerializer(data=request.data)
    print(request.data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data, status=status.HTTP_201_CREATED)
    return  Response({'message': 'Cold Drink Creation Failed'}, status=status.HTTP_400_BAD_REQUEST)   


@api_view(['GET','DELETE', 'PUT'])
def coldrink_details(request, id):
    try:
        drink = ColdDrinks.objects.get(pk=id)
    except ColdDrinks.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if  request.method == 'GET':
        s = ColdDrinksSerializer(drink)
        return Response(s.data)

    if request.method == 'PUT':
        sdata = ColdDrinksSerializer(drink, data=request.data, partial=True)
        if sdata.is_valid():
            sdata.save()
            return Response(sdata.data, status=status.HTTP_202_ACCEPTED)
        return Response(sdata.errors, status=status.HTTP_400_BAD_REQUEST)    

    if request.method == 'DELETE':
        drink.delete()
        return Response({'message': 'Item Deleted'}, status=status.HTTP_200_OK)
              



