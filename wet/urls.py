from django.urls import path 
from .import views


urlpatterns = [
   
    path('',views.index),
    path('find_weather/',views.find_weather),
]
