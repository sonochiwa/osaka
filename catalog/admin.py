from django.contrib import admin
from .models import Clothes, Shoes, ShoesSize, ClothesSize, ClothesCatrgory, ShoesCategory, Review


@admin.register(ClothesSize)
class ClothesSizeAdmin(admin.ModelAdmin):
    list_display = ['size']

@admin.register(ShoesSize)
class ShoesSizeAdmin(admin.ModelAdmin):
    list_display = ['size']

@admin.register(ClothesCatrgory)
class ClothesCatrgoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ShoesCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'count', 'discount', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'count', 'discount', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'date']