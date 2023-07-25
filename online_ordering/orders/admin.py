from django.contrib import admin
from .models import Order, Contact


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'quantity', 'status', 'created_at')
    list_filter = ['status']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'message']
