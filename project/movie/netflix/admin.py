from django.contrib import admin
from .models import movies, Category

# Register your models here.

admin.site.register(movies)
admin.site.register(Category)