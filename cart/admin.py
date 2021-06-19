from django.contrib import admin
from .models import Order, Mart, Promo


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('mart', 'address', 'index',)

@admin.register(Mart)
class MartAdmin(admin.ModelAdmin):
    list_display = ('mart',)

@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('promo',)