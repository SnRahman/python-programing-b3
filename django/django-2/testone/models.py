from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150,null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)