
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('gallery', gallery, name='gallery'),
    path('full-width', full_width, name='full'),
    path('basic-grid', basic_grid, name='basic-grid'),
]