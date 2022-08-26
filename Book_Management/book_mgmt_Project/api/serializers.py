from dataclasses import field
from rest_framework import serializers
from book_mgmt_app.models import Book, Author

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields ='__all__'