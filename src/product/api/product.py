from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, ProductImage, Catalogue, CatalogueProduct
from product.serializers import (
    ProductSerializer,
    ProductImageSerializer,
    CatalogueSerializer,
    CatalogueProductSerializer,
)


# Product List and Create API
class ProductListCreateAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Product Retrieve, Update, and Delete API
class ProductRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def get(self, request, pk):
        product = self.get_object(pk)
        if product:
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        product = self.get_object(pk)
        if product:
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if product:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


# ProductImage List and Create API
class ProductImageListCreateAPIView(APIView):
    def get(self, request, product_id):
        images = ProductImage.objects.filter(product_id=product_id)
        serializer = ProductImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, product_id):
        request.data["product"] = product_id  # Associate the image with the product
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ProductImage Retrieve, Update, and Delete API
class ProductImageRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return ProductImage.objects.get(pk=pk)
        except ProductImage.DoesNotExist:
            return None

    def get(self, request, pk):
        image = self.get_object(pk)
        if image:
            serializer = ProductImageSerializer(image)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        image = self.get_object(pk)
        if image:
            serializer = ProductImageSerializer(image, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        image = self.get_object(pk)
        if image:
            image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
