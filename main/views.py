from django.forms import modelformset_factory
from django.shortcuts import render, redirect

from .forms import *


def index(request):
    return render(request, 'index.html')


def gallery(request):
    return render(request, 'gallery.html')


def full_width(request):
    return render(request, 'full-width.html')


def basic_grid(request):
    return render(request, 'basic-grid.html')


def create_house(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    if request.method == 'POST':
        build_form = BuildingForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if build_form.is_valid():
            build = build_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                Image.objects.create(image=image, building=build)
            return redirect(build.get_absolute_url())
        else:
            build_form = BuildingForm()
            formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'create_house.html', locals())


def update_build(request, pk):
    pass