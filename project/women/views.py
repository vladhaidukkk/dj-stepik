from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone

women = [
    {
        "slug": "ada-lovelace",
        "name": "Ada Lovelace",
        "profession": "Mathematician and writer",
        "birth_year": 1815,
        "death_year": 1852,
        "is_published": True,
    },
    {
        "slug": "marie-curie",
        "name": "Marie Curie",
        "profession": "Physicist and chemist",
        "birth_year": 1867,
        "death_year": 1934,
        "is_published": False,
    },
    {
        "slug": "rosalind-franklin",
        "name": "Rosalind Franklin",
        "profession": "Chemist",
        "birth_year": 1920,
        "death_year": 1958,
        "is_published": True,
    },
]


def home(request):
    context = {"women": women}
    return render(request, "women/index.html", context)


def detail(request, woman_slug):
    woman = next((woman for woman in women if woman["slug"] == woman_slug), None)
    if not woman:
        raise Http404("Woman with this slug doesn't exist")

    context = {"woman": woman}
    return render(request, "women/detail.html", context)


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
