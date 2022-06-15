from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'foods',views.Food)

urlpatterns = [
    path('', views.home, name='home' ),
    path('getrecords', views.get_all_records, name='get_all_records'),
    path('alldrinks', views.get_all_drinks, name='get_all_drinks'),

    path('createdrinks', views.createColdDrinks, name="createColdDrinks"),
    path('drink/<int:id>', views.coldrink_details, name = "coldrink_details"),

    path('item', include(router.urls))
  
]
