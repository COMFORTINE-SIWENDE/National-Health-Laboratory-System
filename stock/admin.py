from django.contrib import admin
from .forms import ProductCreateForm
from .models import Products, Lab, Order, Transaction
# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'category', 'quantity', 'reorder_level', 'unit_of_issue', 'created_by', 'last_updated', 'timestamp')

@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    list_display = ('lab_id', 'lab_name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'staff', 'date')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('product', 'action', 'quantity', 'by_user', 'to', 'date')
