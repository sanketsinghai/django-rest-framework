from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view
from .serializers import StudentSerializer, BookSerializer, CategorySerializer,RegisterSerializer
from .models import Student, Book, Category
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#for jwt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

@api_view()
def home(request):
    return Response({'status code':200, 'message': 'this is trail'})


class RegisterUserAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})
        serializer.save()

        user = User.objects.get(username= serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        #for basic token authentication
        token_obj , _ = Token.objects.get_or_create(user= user)
        return Response({ 'status':200, 'result':serializer.data,'refresh': str(refresh),
        'access': str(refresh.access_token), 'message':'successfully created users'})         


class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_obj = Student.objects.all()
        serializer = StudentSerializer(student_obj, many=True)
        return Response({'status code':200, 'result':serializer.data })
        
    def post(self, request):
        data=request.data
        serializer = StudentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})
        serializer.save()
        return Response({ 'status':200, 'result':data, 'message':'successfully created records'})        
    def put(self, request):
        try:
            #id = request.GET.get(id)
            student_obj = Student.objects.get(id=request.data['id'])
            print(request.data['id'])
            data = request.data
            serializer = StudentSerializer(student_obj, data= request.data)
            if not serializer.is_valid():
                return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})

            serializer.save()
            return Response({ 'status':200, 'result':data, 'message':'successfully created records'})
        except Exception as e:
            print(request.data['id'])
            return Response({ 'status':403, 'message':'invalid id'})

    def delete(self, request):
        try:
            #id = request.GET.get(id)
            student_obj = Student.objects.get(id=request.data['id'])
            student_obj.delete()
            return Response({ 'status':200,  'message':'successfully deleted records'})
        except Exception as e:
            print(request.data['id'])
            return Response({ 'status':403, 'message':'invalid id'})           

class BookAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_obj = Book.objects.all()
        serializer = BookSerializer(student_obj, many=True)
        return Response({'status code':200, 'result':serializer.data })

    def post(self, request):
        data=request.data
        serializer = BookSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})
        serializer.save()
        return Response({ 'status':200, 'result':data, 'message':'successfully created records'})
    
    def put(self, request):
        try:
            #id = request.GET.get(id)
            book_obj = Book.objects.get(id=request.data['id'])
            print(request.data['id'])
            data = request.data
            serializer = BookSerializer(book_obj, data= request.data)
            if not serializer.is_valid():
                return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})

            serializer.save()
            return Response({ 'status':200, 'result':data, 'message':'successfully created records'})
        except Exception as e:
            print(request.data['id'])
            return Response({ 'status':403, 'message':'invalid id'})
    def delete(self, request):
        try:
            #id = request.GET.get(id)
            book_obj = Book.objects.get(id=request.data['id'])
            book_obj.delete()
            return Response({ 'status':200, 'message':'successfully deleted records'})
        except Exception as e:
            print(request.data['id'])
            return Response({ 'status':403, 'message':'invalid id'})           

class CategoryAPI(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        student_obj = Category.objects.all()
        serializer = CategorySerializer(student_obj, many=True)
        return Response({'status code':200, 'result':serializer.data })

    def post(self, request):
        data=request.data
        serializer = CategorySerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})
        serializer.save()
        return Response({ 'status':200, 'result':data, 'message':'successfully created records'})        
    
    def put(self, request):
        try:
            #id = request.GET.get(id)
            category_obj = Category.objects.get(id=request.data['id'])
            print(request.data['id'])
            data = request.data
            serializer = CategorySerializer(category_obj, data= request.data)
            if not serializer.is_valid():
                return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})

            serializer.save()
            return Response({ 'status':200, 'result':data, 'message':'successfully created records'})
        except Exception as e:
            print(request.data['id'])
            return Response({ 'status':403, 'message':'invalid id'})        
    def delete(self, request):
        try:
            #id = request.GET.get(id)
            category_obj = Category.objects.get(id=request.data['id'])
            category_obj.delete()
            return Response({ 'status':200, 'message':'successfully deleted records'})
        except Exception as e:
            print(request.data['id'])
            return Response({ 'status':403, 'message':'invalid id'})         



# @api_view(['GET', 'POST'])
# def index(request):
#     if request.method =='GET':
#         student_obj = Student.objects.all()
#         serializer = StudentSerializer(student_obj, many=True)
#         return Response({'status code':200, 'result':serializer.data })
#     if request.method == 'POST':
#         data=request.data
#         serializer = StudentSerializer(data=request.data)

#         if not serializer.is_valid():
#             return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})
#         serializer.save()
#         return Response({ 'status':200, 'result':data, 'message':'successfully created records'})

# @api_view(['PUT'])
# def update(request,id):
#     try:
#         #id = request.GET.get(id)
#         student_obj = Student.objects.get(id=id)
#         data = request.data
#         serializer = StudentSerializer(student_obj, data= request.data)
#         if not serializer.is_valid():
#             return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})

#         serializer.save()
#         return Response({ 'status':200, 'result':data, 'message':'successfully created records'})
#     except Exception as e:
#         return Response({ 'status':403, 'message':'invalid id'})

# @api_view(['GET', 'POST'])
# def bookdata(request):
#     if request.method =='GET':
#         book_obj = Book.objects.all()
#         serializer = BookSerializer(book_obj, many=True)
#         return Response({'status code':200, 'result':serializer.data })
#     if request.method == 'POST':
#         data=request.data
#         serializer = BookSerializer(data=request.data)

#         if not serializer.is_valid():
#             return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})
#         serializer.save()
#         return Response({ 'status':200, 'result':data, 'message':'successfully created records'})

# @api_view(['GET', 'POST'])
# def categorydata(request):
#     if request.method =='GET':
#         category_obj = Category.objects.all()
#         serializer = CategorySerializer(category_obj, many=True)
#         return Response({'status code':200, 'result':serializer.data })
#     if request.method == 'POST':
#         data=request.data
#         serializer = CategorySerializer(data=request.data)

#         if not serializer.is_valid():
#             return Response({'status code':403, 'error':serializer.errors, 'message':'something went wrong'})
#         serializer.save()
#         return Response({ 'status':200, 'result':data, 'message':'successfully created records'})
