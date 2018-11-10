from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','price',
                    'available','user_name', 'description', 'image', 'created']
    list_filter = ['available', 'created']
    list_editable = ['price', 'available']
admin.site.register(Product, ProductAdmin)
