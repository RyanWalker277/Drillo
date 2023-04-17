from django import forms
from .models import FormSubmission

class FormSubmissionForm(forms.ModelForm):
    class Meta:
        model = FormSubmission
        fields = ('name', 'email', 'message', 'url')