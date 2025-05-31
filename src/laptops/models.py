from django.db import models

# Create your models here.
class laptops(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    image = models.ImageField(upload_to='laptops/images/')
    feature =models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)