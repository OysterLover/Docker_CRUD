from django.contrib import admin

# Register your models here.
from logistic.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass