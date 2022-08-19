from django.contrib import admin
from django.urls import path
from .views import bookList
from book_mgmt_app import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('books/', views.bookList, name='home'),
    path('author/', views.author, name='author'),
    path('about/', views.about, name='about'),
    path('book_create/', views.bookCreate, name='book_create'),
    path('book_update/<str:pk>/', views.bookUpdate, name='book_update'),

]