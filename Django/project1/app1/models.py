from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=15, null=False)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name