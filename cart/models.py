from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product, Size
from django.core.validators import MaxValueValidator


class Promo(models.Model):
    promo = models.CharField(max_length=50)    
    percent = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    mart = models.ForeignKey(Mart, on_delete=models.CASCADE, blank=True, null=True, default=1)
    address = models.CharField(max_length=250, blank=True, null=True)
    index = models.CharField(max_length=6, blank=True, null=True)
    promo = models.CharField(max_length=10, blank=True, null=True)   

    def __str__(self):
        return 'Номер заказа {}'.format(self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='item')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='items')