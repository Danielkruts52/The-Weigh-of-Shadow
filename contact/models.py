from django.db import models

# Create your models here.
class Support(models.Model):
    country = [
        ('USA','USA'),
        ('CA', 'CA')
    ]
    name = models.CharField(max_length=200)
    type = models.CharField(choices=country,default='CA')
    phone_number = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class shop(models.Model):
    country = [
        ("CA","CA"),
        ("USA","USA")
    ]
    type = models.CharField(choices=country,default='CA')
    city = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    def __str__(self):
        return self.address
