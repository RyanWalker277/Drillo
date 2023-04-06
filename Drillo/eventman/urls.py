from django.urls import path
from .views import form_submission, page_preview

urlpatterns = [
    path('submit-form', form_submission, name='form_submission'),
    path('page-preview/<slug:slug>/', page_preview, name='page_preview'),
]