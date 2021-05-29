from django.db import models
from rest_framework import fields, serializers
from .models import Book, Category, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        #fields = ['name', 'age']
        #exclude = ['id', ]
        fields = '__all__'
    #custom validations
    def validate(self, data):
        if data['age']<18:
            raise serializers.ValidationError({"error": "Age must be greater than 18"})
        if data['name']:
            for i in data['name']:
                if i.isdigit():
                    raise serializers.ValidationError({"error": "Name should not contains number"})
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'