from django.db import models


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
    promo = models.ForeignKey(Promo, on_delete=models.CASCADE)    
    mart = models.ForeignKey(Mart, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    index = models.CharField(max_length=6)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'