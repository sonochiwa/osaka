from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product, Size


class Promo(models.Model):
    promo = models.CharField(max_length=10)    
    
    def __str__(self):
        return self.promo

    class Meta:
        verbose_name = 'Промо-код'
        verbose_name_plural = 'Промо-коды'

class Mart(models.Model):
    mart = models.CharField(max_length=70)    
    
    def __str__(self):
        return self.mart

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mart = models.ForeignKey(Mart, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    index = models.CharField(max_length=6)
    promo = models.CharField(max_length=10)   

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='item')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='items')