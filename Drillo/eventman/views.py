from django.shortcuts import render, redirect
from .forms import FormSubmissionForm
from .models import FormSubmission
from django.views.decorators.csrf import csrf_exempt
from django.utils.text import slugify
from django.urls import reverse

@csrf_exempt
def form_submission(request):
    if request.method == 'POST':
        form = FormSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.slug = slugify(submission.title)
            submission.save()
            url = reverse('page_preview', args=[submission.slug])
            return redirect(url)

    else:
        form = FormSubmissionForm()
    return render(request, 'form_submission.jinja', {'form': form})

def page_preview(request,slug):
    submission = FormSubmission.objects.get(slug=slug)
    return render(request, 'rendered-page.jinja', {'submission': submission})

