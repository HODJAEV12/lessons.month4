from django.contrib import admin
from .models import Books

@admin.register(Books)
class AdminBooks(admin.ModelAdmin):
    list_display = ("id", "author", "title", "description", "price", "year", "image")
    search_fields = ("title", "author")
