from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view
from .serializers import StudentSerializer, BookSerializer, CategorySerializer
from .models import Student, Book, Category

@api_view()
def home(request):
    return Response({'status code':200, 'message': 'this is trail'})

@api_view(['GET', 'POST'])
def index(request):
    if request.method =='GET':
        student_obj = Student.objects.all()
        serializer = StudentSerializer(student_obj, many=True)
        return Response({'status code':200, 'result':serializer.data })
    if request.method == 'POST':
        data=request.data
        serializer = StudentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})
        serializer.save()
        return Response({ 'status':200, 'result':data, 'message':'successfully created records'})

@api_view(['PUT'])
def update(request,id):
    try:
        #id = request.GET.get(id)
        student_obj = Student.objects.get(id=id)
        data = request.data
        serializer = StudentSerializer(student_obj, data= request.data)
        if not serializer.is_valid():
            return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})

        serializer.save()
        return Response({ 'status':200, 'result':data, 'message':'successfully created records'})
    except Exception as e:
        return Response({ 'status':403, 'message':'invalid id'})

@api_view(['GET', 'POST'])
def bookdata(request):
    if request.method =='GET':
        book_obj = Book.objects.all()
        serializer = BookSerializer(book_obj, many=True)
        return Response({'status code':200, 'result':serializer.data })
    if request.method == 'POST':
        data=request.data
        serializer = BookSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})
        serializer.save()
        return Response({ 'status':200, 'result':data, 'message':'successfully created records'})

@api_view(['GET', 'POST'])
def categorydata(request):
    if request.method =='GET':
        category_obj = Category.objects.all()
        serializer = CategorySerializer(category_obj, many=True)
        return Response({'status code':200, 'result':serializer.data })
    if request.method == 'POST':
        data=request.data
        serializer = CategorySerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})
        serializer.save()
        return Response({ 'status':200, 'result':data, 'message':'successfully created records'})
