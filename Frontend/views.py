from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def editor(request):
    return render(request, 'editor.html')


def projects(request):
    return render(request, 'projects.html')
