from django.contrib import admin
from .models import Products, ProductImages, ProductBottles,ComboProducts, ContactUs
# Register your models here.


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",   
    )


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "image"
    )

@admin.register(ProductBottles)
class ProductBottlesAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "bottle_size_ml",
        "price",
        "discount_percent",
        "price_after_discount"
    )

@admin.register(ComboProducts)
class ComboProductsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "discription",
        "discounted_price",
        "bottle_sub_total_price",
        "bottle_sub_discounted_price",
    )