from django.contrib import admin
from .models import Department, Degree, User
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User)
admin.site.register(Department)
admin.site.register(Degree)

