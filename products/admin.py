from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_available', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['is_available']
    search_fields = ['name', 'description']