from django.contrib import admin
from django.urls import path,include
from . views import *

urlpatterns = [
    path('', home),
    path('api/v1/students', index),
    path('api/v1/students/<id>/', update),
    path('api/v1/books', bookdata),
    path('api/v1/catergory', categorydata),
]
