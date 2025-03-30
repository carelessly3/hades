from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Product, ProductImage, Catalogue, CatalogueProduct


# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "company",
        "category",
        "price",
        "moq",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "company__name", "category")
    list_filter = ("created_at", "updated_at", "category")
    readonly_fields = ("created_at", "updated_at")

    # Add fieldsets for better organization in the admin panel
    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "company",
                    "name",
                    "description",
                    "hsn_code",
                    "category",
                    "fiber_content",
                    "construction",
                    "type",
                )
            },
        ),
        (
            "Pricing and Stock",
            {
                "fields": (
                    "price",
                    "moq",
                    "stock_quantity",
                    "stock_lot",
                    "manufacturing_lead_time",
                )
            },
        ),
        (
            "Additional Information",
            {"fields": ("special_features", "carbon_footprint_details")},
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )


# Register the ProductImage model
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "image_url", "created_at", "updated_at")
    search_fields = ("product__name",)
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Image Information", {"fields": ("product", "image_url")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )


# Register the Catalogue model
@admin.register(Catalogue)
class CatalogueAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "created_at", "updated_at")
    search_fields = ("name", "company__name")
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Catalogue Information", {"fields": ("company", "name", "description")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )


# Register the CatalogueProduct model
@admin.register(CatalogueProduct)
class CatalogueProductAdmin(admin.ModelAdmin):
    list_display = ("catalogue", "product", "created_at", "updated_at")
    search_fields = ("catalogue__name", "product__name")
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Catalogue Product Information", {"fields": ("catalogue", "product")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
