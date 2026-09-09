from django.contrib import admin
from .models import Test

@admin.register(Test)
class AdminTest(admin.ModelAdmin):
    list_display = ("id", "name", "age")
    search_fields = ("name", "age")