from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime

class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название"
    )
    slug = models.SlugField(max_length=40, unique=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название"
    )
    slug = models.SlugField(max_length=40, unique=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    year = models.SmallIntegerField(verbose_name="Год выхода", validators=[MaxValueValidator(datetime.now().year)])
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Категория"
    )
    genre = models.ManyToManyField(Genre, blank=True, related_name='titles', verbose_name="Жанр")

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
