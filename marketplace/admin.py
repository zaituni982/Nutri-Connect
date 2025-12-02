from django.contrib import admin
from .models import FoodItem

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'farmer', 'quantity', 'price', 'status', 'expiry_date', 'created_at')
    list_filter = ('status', 'expiry_date')
    search_fields = ('name', 'farmer__username')

admin.site.register(FoodItem, FoodItemAdmin)

