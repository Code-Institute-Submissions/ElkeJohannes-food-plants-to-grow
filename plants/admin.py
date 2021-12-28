from django.contrib import admin

from .models import Category, Plant

# Register your models here.
admin.site.register(Plant)
admin.site.register(Category)