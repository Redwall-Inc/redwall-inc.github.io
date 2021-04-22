from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.Charfield(max_length=255)
    price = models.Floatfield()
    stock = models.Integerfield()
    image url