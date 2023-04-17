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
            submission.save()
            url = submission.url
            return redirect(reverse('page_preview', kwargs={'slug': url}))

    else:
        form = FormSubmissionForm()
    return render(request, 'create.html', {'form': form})

def page_preview(request,url):
    submission = FormSubmission.objects.get(url=url)
    return render(request, 'rendered-page.html', {'submission': submission})