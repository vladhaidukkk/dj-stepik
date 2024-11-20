from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Women(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category)
    description = models.TextField(blank=True)
    birth_year = models.IntegerField()
    death_year = models.IntegerField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
