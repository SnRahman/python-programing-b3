from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.id} - {self.name}'


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    # category = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product-imgs/' )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)