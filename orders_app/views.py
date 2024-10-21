from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import Orders
from .forms import OrderProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.


class MyOrderView(LoginRequiredMixin, DetailView):
    model= Orders
    template_name='orders_app/order_details.html'
    context_object_name='orders'
    

    def get_object(self, queryset=None):
        return Orders.objects.filter(is_active=True, user=self.request.user).first()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        context['total_price'] = order.precio_total()
        return context

class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = "orders_app/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy("MyOrderView")

    def form_valid(self, form):
        order, _ = Orders.objects.get_or_create(
            is_active=True,
            user=self.request.user,
        )
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)