from django.contrib import admin
from .models import Customer, Product, Invoice, InvoiceItem

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
