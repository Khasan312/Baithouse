from django.urls import include, path

from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("gallery/", BuiltListView.as_view(), name="gallery"),
    path("full-width/", full_width, name="full"),
    path("basic-grid/", basic_grid, name="basic-grid"),
    path("create-house/", create_house, name="create-house"),
    path("update-house/<int:pk>/", update_build, name="update-house"),
    path("delete-house/<int:pk>/", delete_build, name='delete-house'),
    path("about-us/", about_us, name="about-us"),
]
