from django.db import models

# Create your models here.
class Support(models.Model):
    country = [
        ('USA','USA'),
        ('CA', 'CA')
    ]
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=3, choices=country, default='CA')  # Добавил max_length=3
    phone_number = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class shop(models.Model):
    country = [
        ("CA","CA"),
        ("USA","USA")
    ]
    type = models.CharField(max_length=3, choices=country, default='CA')  # Добавил max_length=3
    city = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    def __str__(self):
        return self.address

class office(models.Model):
    country = [
        ("CA","CA"),
        ("USA","USA")
    ]
    name = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=3, choices=country, default='CA')  # Добавил max_length=3
    city = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class community(models.Model):
    country = [
        ("CA","CA"),
        ("USA","USA")
    ]
    type = models.CharField(max_length=3, choices=country, default='CA')  # Добавил max_length=3
    city = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    def __str__(self):
        return self.address
