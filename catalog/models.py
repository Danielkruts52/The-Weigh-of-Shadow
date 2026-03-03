from django.db import models

class Collections(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=200, default='black')
    text = models.TextField(default='about')
    def __str__(self):
        return self.name
class SpecialCollections(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(default='about')
    def __str__(self):
        return self.name
    
class T_shirt(models.Model):
    type = [
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL")
    ]
    image = models.ImageField
    image2 = models.URLField(max_length=250)
    name = models.CharField(max_length=100)
    structure = models.CharField(max_length=100, default='cotton')
    price = models.CharField(max_length=20)
    size = models.CharField(default='M', choices= type)
    text = models.TextField('about')
    def __str__(self):
        return self.name

class Sweatshirt(models.Model):
    type = [
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL")
    ]
    image = models.ImageField
    image2 = models.URLField(max_length=250)
    name = models.CharField(max_length=100)
    structure = models.CharField(max_length=100, default='cotton')
    price = models.CharField(max_length=20)
    size = models.CharField(default='M', choices= type)
    text = models.TextField('about')
    def __str__(self):
        return self.name





    
    