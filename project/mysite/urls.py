from django.contrib import admin
from django.http import HttpResponseNotFound
from django.urls import include, path

urlpatterns = [
    path("", include("women.urls")),
    path("admin/", admin.site.urls),
]


def handler404(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
