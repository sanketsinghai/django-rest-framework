from django.contrib import admin
from django.urls import path,include
from . views import *

urlpatterns = [
    path('', home),
    path('api/v1/students', StudentAPI.as_view()),
    path('api/v1/books', BookAPI.as_view()),
    path('api/v1/category', CategoryAPI.as_view()),
    path('api/v1/register', RegisterUserAPI.as_view()),
    
    #for function based
    # path('api/v1/students', index),
    # path('api/v1/students/<id>/', update),
    # path('api/v1/books', bookdata),
    # path('api/v1/catergory', categorydata),
]
