from django.db import models
from django.utils.text import slugify

from apps.core.models import BaseModel


class Category(BaseModel, models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', ]
        verbose_name_plural = 'Categories'


class ProductManager(models.Manager):
    def is_active(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Product(BaseModel, models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='product')
    description = models.TextField()
    price = models.FloatField()
    added = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = ProductManager

    class Meta:
        ordering = ("-added",)

    def __str__(self):
        return self.title


