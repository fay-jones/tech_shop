from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description= models.TextField()
    image = models.ImageField(upload_to='products/',blank=True,null=True)
    stock =models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.PositiveBigIntegerField(max_length=9)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.email}" 