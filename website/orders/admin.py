from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'paid']
    list_filter = ['paid']


admin.site.register(Order, OrderAdmin)