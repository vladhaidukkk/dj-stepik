from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone


def index(request):
    return HttpResponse("<h1>Index page</h1>")


def categories(request):
    return HttpResponse("<h1>Categories page</h1>")


def category_by_id(request, cat_id):
    return HttpResponse(f"<h1>Category page</h1><p>id: {cat_id}</p>")


def category_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Category page</h1><p>slug: {cat_slug}</p>")


def categories_archive(request, year):
    current_year = timezone.now().year
    if current_year < year:
        uri = reverse("categories_archive", kwargs={"year": current_year})
        return redirect(uri)
    return HttpResponse(f"<h1>Categories archieve page</h1><p>year: {year}</p>")
