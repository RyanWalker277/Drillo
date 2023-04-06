from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import FormSubmission

admin.site.register(FormSubmission)
