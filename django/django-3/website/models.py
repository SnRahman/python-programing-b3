from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='website/')

    def __str__(self):
        return f'{self.title}'