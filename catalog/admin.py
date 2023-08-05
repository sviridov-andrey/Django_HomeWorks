from django.contrib import admin
from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    list_filter = ('category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('product_name', 'product_description',)


@admin.register(Version)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'version_is_active',)
    list_filter = ('version_number', 'version_is_active',)
    search_fields = ('version_number', 'version_is_active',)
