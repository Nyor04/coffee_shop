
from django.urls import path
from . import  views


urlpatterns = [
    path('', views.ProductListView.as_view(), name="list_product"),
    path('api', views.ProductListAPI.as_view(), name="list_product_api"),
    path('add_product/', views.ProductFormView.as_view(), name="add_product"),
]
