from django.db import models
from django.contrib.auth.models import User
from products_app.models import Product
# Create your models here.
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order {self.id}"
    
    def precio_total(self):
        total = 0
        for order_product in self.orderproduct_set.all():
            total += order_product.quantity * order_product.product.price
        
        return total
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} {self.product}"
