from django.urls import path, register_converter

from . import converters, views

register_converter(converters.FourDigitYearConverter, "yyyy")

app_name = "women"
urlpatterns = [
    path("", views.home, name="home"),
    path("categories/<str:category_name>", views.category, name="category"),
    path("about/", views.about, name="about"),
    path("women/<slug:woman_slug>", views.detail, name="detail"),
]
