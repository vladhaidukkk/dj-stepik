from django.http import Http404
from django.shortcuts import render

women = [
    {
        "slug": "ada-lovelace",
        "name": "Ada Lovelace",
        "profession": "Mathematician and writer",
        "description": (
            "Ada Lovelace is often considered the first computer programmer for her work on Charles Babbage's early "
            "mechanical general-purpose computer, the Analytical Engine. She recognized the machine's potential beyond "
            "mere calculation and envisioned its use for more complex tasks."
        ),
        "birth_year": 1815,
        "death_year": 1852,
        "is_published": True,
    },
    {
        "slug": "marie-curie",
        "name": "Marie Curie",
        "profession": "Physicist and chemist",
        "description": (
            "Marie Curie was a pioneering scientist known for her research on radioactivity. She was the first woman "
            "to win a Nobel Prize and remains the only person to win Nobel Prizes in two different scientific "
            "fields: Physics and Chemistry."
        ),
        "birth_year": 1867,
        "death_year": 1934,
        "is_published": False,
    },
    {
        "slug": "rosalind-franklin",
        "name": "Rosalind Franklin",
        "profession": "Chemist",
        "description": (
            "Rosalind Franklin was a chemist whose work with X-ray diffraction was critical to the discovery of the "
            "DNA double helix. Her contributions to molecular biology were significant, and she is now recognized as a "
            "key figure in the field."
        ),
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
