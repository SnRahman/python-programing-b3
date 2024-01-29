from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150,null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.first_name} - {self.email}'



class Employee(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=150 )

    def __str__(self):
        return f'{self.id} - {self.f_name} - {self.email}'
