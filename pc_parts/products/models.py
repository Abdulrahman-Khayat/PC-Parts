from django.db import models
import uuid
import json
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    class Meta:
        verbose_name_plural = "categories"
        db_table = "categories"

class Brand(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = "brands"
        db_table = "brands"

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    category = models.ForeignKey(Category, to_field="id", null=False, related_name='products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, null=False, related_name='products', on_delete=models.CASCADE)


    def __str__(self):
        return f'{{"name"="{self.name}", "description"="{self.description}", "price"={self.price}}}'
    
    class Meta:
        verbose_name_plural = "products"
        db_table = "products"


