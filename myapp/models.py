from django.db import models

class Form(models.Model):
    DATA_CHOICES = [
        ('Order and delivery', 'Order and delivery'),
        ('Product', 'Product'),
        ('Website', 'Website'),
        ('Refund and exchange', 'Refund and exchange'),
        ('Other', 'Other'),
    ]
    
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    type = models.CharField(max_length=50, choices=DATA_CHOICES, default='Other')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return f"{self.name} - {self.created_at}"


