from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'brand', 'price', 'discount_price', 'timestamp']
    search_fields = ['__str__', 'slug', 'brand', 'price', 'discount_price', 'timestamp']


admin.site.register(Product, ProductAdmin)
