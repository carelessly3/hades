from django.db import models

# Create your models here.

from django.db import models
from hades.helpers.models import BaseModel
from company.models import Company


class Product(BaseModel):
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    hsn_code = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    fiber_content = models.CharField(max_length=100, blank=True, null=True)
    construction = models.TextField(blank=True, null=True)
    TYPE_CHOICES = [
        ("handcrafted", "Handcrafted"),
        ("machine_made", "Machine Made"),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    special_features = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    moq = models.IntegerField()
    stock_quantity = models.IntegerField(blank=True, null=True)
    stock_lot = models.CharField(max_length=100, blank=True, null=True)
    manufacturing_lead_time = models.IntegerField(blank=True, null=True)
    carbon_footprint_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image_url = models.URLField()

    def __str__(self):
        return f"Image for {self.product.name}"


class Catalogue(BaseModel):
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class CatalogueProduct(BaseModel):
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} in {self.catalogue.name}"
