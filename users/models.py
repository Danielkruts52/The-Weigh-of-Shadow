from django.db import models
from django.contrib.auth.models import User
from catalog.models import T_shirt, Sweatshirt

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

    def get_total_price(self):
        total = 0
        for item in self.items.all():
            total += item.get_total_price()
        return total

class CartItem(models.Model):
    SIZE_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]
    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    
    # Полиморфная связь - товар может быть либо футболкой, либо толстовкой
    t_shirt = models.ForeignKey(T_shirt, on_delete=models.CASCADE, null=True, blank=True)
    sweatshirt = models.ForeignKey(Sweatshirt, on_delete=models.CASCADE, null=True, blank=True)
    
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=5, choices=SIZE_CHOICES, default='S')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.t_shirt:
            return f"{self.t_shirt.name} - {self.size} x{self.quantity}"
        elif self.sweatshirt:
            return f"{self.sweatshirt.name} - {self.size} x{self.quantity}"
        return "Cart item"

    def get_item(self):
        """Возвращает товар (футболку или толстовку)"""
        if self.t_shirt:
            return self.t_shirt
        return self.sweatshirt

    def get_price(self):
        """Возвращает цену товара с учетом размера"""
        item = self.get_item()
        if not item:
            return 0
            
        # Парсим цену из строки
        price_str = item.price
        # Убираем пробелы, заменяем запятую на точку, убираем $
        price_str = price_str.replace(' ', '').replace(',', '.').replace('$', '')
        
        try:
            base_price = float(price_str)
        except ValueError:
            base_price = 0
        
        # Добавляем цену за размер
        size_prices = {
            'S': 0,
            'M': 10,
            'L': 20,
            'XL': 30,
            'XXL': 40
        }
        return base_price + size_prices.get(self.size, 0)

    def get_total_price(self):
        """Возвращает общую цену (цена * количество)"""
        return self.get_price() * self.quantity

    class Meta:
        unique_together = ['cart', 't_shirt', 'sweatshirt', 'size']