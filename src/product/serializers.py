from rest_framework import serializers
from .models import Product, ProductImage, Catalogue, CatalogueProduct


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at", "deleted_at")


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(
        many=True, read_only=True
    )  # Nested serializer for images

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at", "deleted_at")


class CatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogue
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at", "deleted_at")


class CatalogueProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogueProduct
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at", "deleted_at")
