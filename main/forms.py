from datetime import datetime

from django import forms

from .models import Build, Image


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Build
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )
