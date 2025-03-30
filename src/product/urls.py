from django.urls import path
from product.api.catalogue import (
    CatalogueListCreateAPIView,
    CatalogueRetrieveUpdateDestroyAPIView,
    CatalogueProductListCreateAPIView,
    CatalogueProductRetrieveUpdateDestroyAPIView,
)

from product.api.product import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    ProductImageListCreateAPIView,
    ProductImageRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    # Product endpoints
    path("products/", ProductListCreateAPIView.as_view(), name="product-list-create"),
    path(
        "products/<int:pk>/",
        ProductRetrieveUpdateDestroyAPIView.as_view(),
        name="product-retrieve-update-destroy",
    ),
    # ProductImage endpoints
    path(
        "products/<int:product_id>/images/",
        ProductImageListCreateAPIView.as_view(),
        name="product-image-list-create",
    ),
    path(
        "images/<int:pk>/",
        ProductImageRetrieveUpdateDestroyAPIView.as_view(),
        name="product-image-retrieve-update-destroy",
    ),
    # Catalogue endpoints
    path(
        "catalogues/",
        CatalogueListCreateAPIView.as_view(),
        name="catalogue-list-create",
    ),
    path(
        "catalogues/<int:pk>/",
        CatalogueRetrieveUpdateDestroyAPIView.as_view(),
        name="catalogue-retrieve-update-destroy",
    ),
    # CatalogueProduct endpoints
    path(
        "catalogues/<int:catalogue_id>/products/",
        CatalogueProductListCreateAPIView.as_view(),
        name="catalogue-product-list-create",
    ),
    path(
        "catalogue-products/<int:pk>/",
        CatalogueProductRetrieveUpdateDestroyAPIView.as_view(),
        name="catalogue-product-retrieve-update-destroy",
    ),
]
