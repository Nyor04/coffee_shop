from django.urls import path
from .views import MyOrderView,CreateOrderProductView

urlpatterns = [
    path("my_orders", MyOrderView.as_view(), name="MyOrderView"),
    path("create_order", CreateOrderProductView.as_view(), name="create_order"),
]
