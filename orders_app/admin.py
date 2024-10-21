from django.contrib import admin
from . import models

# Register your models here.
class OrderProductInLineAdmin(admin.TabularInline):
    model=models.OrderProduct
    extra=0

class OrdersAdmin(admin.ModelAdmin):
    model=models.Orders
    inlines=[OrderProductInLineAdmin]


admin.site.register(models.Orders, OrdersAdmin)