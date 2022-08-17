from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class Book(models.Model):
    name=models.CharField(max_length=255, null=False)
    author=models.ForeignKey(Author, related_name='book_author', on_delete=models.SET_NULL, null=True)
    published_year=models.DateField()

    def __str__(self):
        return self.name
