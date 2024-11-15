from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone

famous_women = [
    {
        "name": "Ada Lovelace",
        "profession": "Mathematician and writer",
        "birth_year": 1815,
        "death_year": 1852,
        "is_published": True,
    },
    {
        "name": "Marie Curie",
        "profession": "Physicist and chemist",
        "birth_year": 1867,
        "death_year": 1934,
        "is_published": False,
    },
    {
        "name": "Rosalind Franklin",
        "profession": "Chemist",
        "birth_year": 1920,
        "death_year": 1958,
        "is_published": True,
    },
]


def index(request):
    context = {"title": "Index Page", "famous_women": famous_women}
    return render(request, "women/index.html", context)


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
