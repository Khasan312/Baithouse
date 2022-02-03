from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render

from .forms import *


def index(request):
    return render(request, "index.html")


def gallery(request):
    obj = Build.objects.all()
    return render(request, "gallery.html", locals())


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
    build = get_object_or_404(Build, pk=pk)
    image = get_object_or_404(Image, building=build)

    ImageFormSet = ImageForm(
        request.POST or None, request.FILES or None, instance=image
    )
    build_form = BuildingForm(request.POST or None, instance=build)

    if build_form.is_valid() and ImageFormSet.is_valid():
        build_form.save()
        ImageFormSet.save()
        return redirect(build.get_absolute_url())

    return render(
        request,
        "update_build.html",
        context={"image_form": ImageFormSet, "build_form": build_form},
    )


def delete_build(request, pk):
    pass


def about_us(request):
    return render(request, "about-us.html")
