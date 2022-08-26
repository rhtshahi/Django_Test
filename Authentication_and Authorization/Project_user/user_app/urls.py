from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.logoutUser, name='user-page'),
]