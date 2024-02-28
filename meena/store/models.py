from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return f'{self.id} - {self.title}'

class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    sub_total = models.DecimalField(max_digits=10,decimal_places=2)
    order_id = models.CharField(default=0,max_length=15)

class Order(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150,null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
