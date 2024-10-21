from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _ 


# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name="nombre")
    description = models.TextField(max_length=200, verbose_name="descripción")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="precio")
    available = models.BooleanField(default=True, verbose_name="disponibilidad")
    photo = models.ImageField(null=True,blank=True,verbose_name="foto")

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})
