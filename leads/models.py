from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)



class Product(models.Model):
    name= models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    regular_price = models.IntegerField()
    discount_price = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)