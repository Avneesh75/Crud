from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=60)
    roll = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
