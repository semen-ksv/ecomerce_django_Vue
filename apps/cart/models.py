from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from apps.store.models import Product

#
# class Cart(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
#     product_id = models.ManyToManyField(Product, related_name='cart')