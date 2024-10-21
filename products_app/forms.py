
from django import forms
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="nombre")
    description = forms.CharField(max_length=200, label="descripción")
    price = forms.DecimalField(max_digits=5, decimal_places=2, label="precio")
    available = forms.BooleanField(initial=True, label="disponibilidad",required=False)
    photo = forms.ImageField(label="imagen del producto",required=False)

    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            available=self.cleaned_data["available"],
            photo=self.cleaned_data["photo"]
        )