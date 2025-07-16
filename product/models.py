from django.db import models

from account.models import CustomUser
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateField(auto_now_add=True) 
    customer = models.ForeignKey(CustomUser, related_name='products', on_delete=models.CASCADE, blank=True)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.title

