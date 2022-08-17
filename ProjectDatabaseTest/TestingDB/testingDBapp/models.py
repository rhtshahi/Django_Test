from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null=False)
    dob = models.DateField()
    level = models.CharField(max_length=50)