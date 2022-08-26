from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from book_mgmt_app.models import Book
from .serializers import BookSerializers

# Create your views here.
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List': '/book-list/',
        'Detail':'/book-detail/<str:pk>/',
        'Create': '/add-book/',
        'Update': '/update-book/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def BookList(request):
    bookList = Book.objects.all()
    serializer = BookSerializers(bookList, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def BookDetail(request, pk):
    bookList = Book.objects.get(id=pk)
    serializer = BookSerializers(bookList, many=False)
    return Response(serializer.data)