from django.contrib import admin
from .models import Order, OrderItem, Mart, Promo

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('mart', 'address', 'index',)
    inlines = [OrderItemAdmin]

@admin.register(Mart)
class MartAdmin(admin.ModelAdmin):
    list_display = ('mart',)

@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('promo',)