from django.db import models

# Create your models here.
from django.utils.text import slugify


class BaseModel():
    title = None
    slug = None


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)