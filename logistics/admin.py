from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'food_item', 'buyer', 'quantity', 'payment_status', 'pickup_status', 'created_at')
    list_filter = ('pickup_status', 'payment_status')
    search_fields = ('food_item__name', 'buyer__username')

admin.site.register(Order, OrderAdmin)

