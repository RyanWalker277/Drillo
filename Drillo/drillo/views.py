from django.shortcuts import render

def home(request):
    context = {'title': 'My Page'}
    return render(request, 'index.html', context)
