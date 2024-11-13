from django.urls import path, register_converter

from . import converters, views

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("", views.index, name="index"),
    path("cats/", views.categories, name="categories"),
    path("cats/<int:cat_id>/", views.category_by_id, name="category_by_id"),
    path("cats/<slug:cat_slug>/", views.category_by_slug, name="category_by_slug"),
    path("archive/cats/<yyyy:year>/", views.categories_archive, name="categories_archive"),
]
