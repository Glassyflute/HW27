from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=70)
    author = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    description = models.SlugField(max_length=700)
    address = models.SlugField(max_length=100)
    is_published = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=20)

