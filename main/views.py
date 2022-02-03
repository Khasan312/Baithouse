from django.forms import modelformset_factory
from django.shortcuts import redirect, render

from .forms import *


def index(request):
    return render(request, "index.html")


def gallery(request):
    return render(request, "gallery.html")


def full_width(request):
    return render(request, "full-width.html")


def basic_grid(request):
    return render(request, "basic-grid.html")


def create_house(request):
    build_form = BuildingForm()
    image_form = UploadImageForm()

    if request.method == "POST":
        build_form = BuildingForm(request.POST)
        image_form = UploadImageForm(request.POST, request.FILES)

        if build_form.is_valid() and image_form.is_valid():
            build = build_form.save()

            image_object = Image.objects.create(
                image=image_form.cleaned_data["image"], building=build
            )
            image_object.save()

            return redirect(build.get_absolute_url())
        else:
            build_form = BuildingForm()
            image_form = UploadImageForm()

    return render(
        request,
        "create_house.html",
        {"build_form": build_form, "image_form": image_form},
    )


def update_build(request, pk):
    pass
