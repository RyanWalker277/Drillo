from django.urls import path
from .views import form_submission, page_preview

urlpatterns = [
    path('create', form_submission, name='form_submission'),
    path('<slug:url>/', page_preview, name='page_preview'),
]