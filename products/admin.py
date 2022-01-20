from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'inventory']
    list_editable = ['price']
    list_per_page = 10


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer', 'quantity', 'date']


admin.site.register(models.Category)
