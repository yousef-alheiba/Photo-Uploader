from django.urls import path
from .views import *
urlpatterns = [
    path('',listphoto,name='listphoto'),
    path('add/',addphoto,name='addphoto'),
    path('delete/<str:pk>/',deletephoto,name='deletephoto'),
    path('update/<str:pk>/',updatephoto,name='updatephoto'),
]