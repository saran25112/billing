from django.contrib import admin
from .models import Bill,Supplier # Import the Bill model from models.py

admin.site.register(Supplier)

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier_name', 'customer_name', 'item_name', 'payment_method', 'total_amount', 'created_at')
    readonly_fields = ('total_amount', 'created_at')
    search_fields = ('supplier_name', 'customer_name', 'item_name')
    list_filter = ('payment_method', 'created_at')
    ordering = ('-created_at',)
