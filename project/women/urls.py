from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cats/", views.categories, name="categories"),
    path("cats/<int:cat_id>/", views.category_by_id, name="category_by_id"),
    path("cats/<slug:cat_slug>/", views.category_by_slug, name="category_by_slug"),
    re_path("^archive/cats/(?P<year>[0-9]{4})/", views.categories_archive, name="categories_archive"),
]
