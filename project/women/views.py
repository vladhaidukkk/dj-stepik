from django.http import Http404
from django.shortcuts import render

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


def about(request):
    return render(request, "women/about.html")


def detail(request, woman_slug):
    woman = next((woman for woman in women if woman["slug"] == woman_slug), None)
    if not woman:
        raise Http404("Woman with this slug doesn't exist")

    context = {"woman": woman}
    return render(request, "women/detail.html", context)
