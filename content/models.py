from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=200,
    )
    slug = models.SlugField(max_length=40, unique=True)

    class Meta:
        ordering = ('id',)


class Genre(models.Model):
    name = models.CharField(
        max_length=200
    )
    slug = models.SlugField(max_length=40, unique=True)

    class Meta:
        ordering = ('id',)


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.SmallIntegerField()
    description = models.TextField(
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
