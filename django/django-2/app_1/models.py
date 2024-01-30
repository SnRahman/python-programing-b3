from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id}--{self.first_name}--{self.email}'