from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Hero

@admin.register(Hero)
class CustomAdminClass(ModelAdmin):
    pass