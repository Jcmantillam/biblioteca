from django.db import models
from django.db.models import F, Q
from .constants import last_day_of_year

class Editor(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    


class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=500, unique=True)
    subtitle = models.CharField(max_length=500, unique=True)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    release_date = models.DateField()
    image = models.ImageField(upload_to="covers", blank=True)
    editor = models.ForeignKey(Editor, on_delete=models.PROTECT)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(release_date__lte=last_day_of_year),
                name=F"La Fecha máxima válida es {last_day_of_year}"
            )
        ]