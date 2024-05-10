from django.db import models

# Create your models here.
class Student(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    phone = models.IntegerField()
    dob = models.DateField()