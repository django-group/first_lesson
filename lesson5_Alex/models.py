from django.db import models

# Create your models here.


class Human(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    company = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=6, decimal_places=2)