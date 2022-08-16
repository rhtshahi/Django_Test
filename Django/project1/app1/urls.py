from django.contrib import admin
from django.urls import path
from app1 import views
from .views import about

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
]