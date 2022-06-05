from django.urls import path
from .views import homePage,carDetailView,ajax_deneme,testView
urlpatterns = [
    path('',homePage,name='home'),
    path('car/<int:pk>/',carDetailView,name='car_detail'),
    path('map/',ajax_deneme,name='map'),
    path('map/test',testView,name='test'),
]