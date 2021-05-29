from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=100)

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category_name

class Book(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)