from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel

class Size(models.Model):
    size = models.CharField(max_length=200)

    def __str__(self):
        return self.size

class ClothesSize(Size):
    class Meta:
        verbose_name = 'Clothes Sizes'
        verbose_name_plural = 'Clothes Sizes'

class ShoesSize(Size):
    class Meta:
        verbose_name = 'Shoes Sizes'
        verbose_name_plural = 'Shoes Sizes'

class Category(PolymorphicModel):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_list_by_category', args=[self.slug])

class ClothesCatrgory(Category):
    class Meta:
        verbose_name = 'Clothes Categories'
        verbose_name_plural = 'Clothes Categories'
    
class ShoesCategory(Category):
    class Meta:
        verbose_name = 'Shoes Categories'
        verbose_name_plural = 'Shoes Categories'

class Product(PolymorphicModel):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    count = models.IntegerField(null=True)
    discount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse('catalog:product_detail', args=[self.id, self.slug])
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def discount_calc(self):
        return self.price - (self.price * self.discount / 100)

class Clothes(Product):
    category = models.ForeignKey(ClothesCatrgory, related_name='products',
        on_delete=models.CASCADE)
    sizes = models.ManyToManyField(ClothesSize, related_name='products')
    class Meta:
        verbose_name = 'Clothes'
        verbose_name_plural = 'Clothes'

class Shoes(Product):
    category = models.ForeignKey(ShoesCategory, related_name='products',
        on_delete=models.CASCADE)
    sizes = models.ManyToManyField(ShoesSize, related_name='products')
    class Meta:
        verbose_name = 'Shoes'
        verbose_name_plural = 'Shoes'

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
