from tkinter import CASCADE
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Department(models.Model):
    dept_name=models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.dept_name

class Degree(models.Model):
    course=models.CharField(max_length=255, null=False, blank=False)
    duration=models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.course

class User(AbstractUser):
    gender = models.CharField(max_length=10, choices=[('Male', 'M'), ('Female', 'F'), ('Other', 'O')])
   # email = models.EmailField(max_length=255, unique=True)
    contact = models.CharField(max_length=20, unique=True, null=True)
    dept_name = models.ForeignKey(Department, related_name='department', on_delete=models.SET_NULL, null=True)
    course_name = models.ForeignKey(Degree, related_name='course_name', on_delete=models.SET_NULL, null=True)