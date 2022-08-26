from ast import pattern
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.apiOverView, name='api-overview'),
    path('book-list/', views.BookList, name='book-list'),
    path('book-detail/<str:pk>/', views.BookDetail, name='book-detail'),
]