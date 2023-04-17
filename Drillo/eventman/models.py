from django.db import models
from django.urls import reverse

class FormSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    url = models.SlugField(unique=True, max_length=255)

    def save(self, *args, **kwargs):
        self.slug = f"{self.name.replace(' ', '-').lower()}-{self.name.replace(' ', '-').lower()}"
        super(FormSubmission, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('page_preview', args=[self.slug])
