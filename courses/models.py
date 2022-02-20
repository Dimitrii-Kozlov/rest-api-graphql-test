from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    available = models.BooleanField()