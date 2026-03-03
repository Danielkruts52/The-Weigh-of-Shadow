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
    
