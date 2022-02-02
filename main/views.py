from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def gallery(request):
    return render(request, 'gallery.html')


def full_width(request):
    return render(request, 'full-width.html')


def basic_grid(request):
    return render(request, 'basic-grid.html')

