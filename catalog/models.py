from django.db import models

class Collections(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=200, default='black')
    text = models.TextField(default='about')
    def __str__(self):
        return self.name
class SpecialCollections(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=200, default='black')
    text = models.TextField(default='about')
    def __str__(self):
        return self.name
    
class T_shirt(models.Model):
    type_collections = [
        ("Modern Minimalism", "Modern Minimalism"),
        ("The promise of hope","The promise of hope"),
        ("The Crying Machiavelli", "The Crying Machiavelli"),
        ("Blood money", "Blood money")
    ]
    image = models.ImageField(default='null', blank=True, null= True)
    image2 = models.URLField(max_length=250, blank= True, null=True)
    name = models.CharField(max_length=100)
    structure = models.CharField(max_length=100, default='cotton')
    price = models.CharField(max_length=20)
    collections_type = models.CharField(default='Modern Minimalism',choices=type_collections)
    text = models.TextField('about')
    def __str__(self):
        return self.name

class Sweatshirt(models.Model):
    type_collections = [
        ("Modern Minimalism", "Modern Minimalism"),
        ("The promise of hope","The promise of hope"),
        ("The Crying Machiavelli", "The Crying Machiavelli"),
        ("Blood money", "Blood money")
    ]
    image = models.ImageField(default='null', blank=True, null= True)
    image2 = models.URLField(max_length=250, blank=True, null= True)
    name = models.CharField(max_length=100)
    structure = models.CharField(max_length=100, default='cotton')
    price = models.CharField(max_length=20)
    collections_type = models.CharField(default='Modern Minimalism',choices=type_collections)
    text = models.TextField('about')
    def __str__(self):
        return self.name





    
    