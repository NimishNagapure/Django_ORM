from django.db import models

# Create your models here.

from django.db import models


class Teacher(models.Model):
      
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class Student(models.Model):
      
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.ForeignKey(Teacher,models.DO_NOTHING)

    def __str__(self):
        return self.firstname



class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
