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


# Catalogue List and Create API
class CatalogueListCreateAPIView(APIView):
    def get(self, request):
        catalogues = Catalogue.objects.all()
        serializer = CatalogueSerializer(catalogues, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CatalogueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Catalogue Retrieve, Update, and Delete API
class CatalogueRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Catalogue.objects.get(pk=pk)
        except Catalogue.DoesNotExist:
            return None

    def get(self, request, pk):
        catalogue = self.get_object(pk)
        if catalogue:
            serializer = CatalogueSerializer(catalogue)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        catalogue = self.get_object(pk)
        if catalogue:
            serializer = CatalogueSerializer(catalogue, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        catalogue = self.get_object(pk)
        if catalogue:
            catalogue.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


# CatalogueProduct List and Create API
class CatalogueProductListCreateAPIView(APIView):
    def get(self, request, catalogue_id):
        catalogue_products = CatalogueProduct.objects.filter(catalogue_id=catalogue_id)
        serializer = CatalogueProductSerializer(catalogue_products, many=True)
        return Response(serializer.data)

    def post(self, request, catalogue_id):
        request.data["catalogue"] = (
            catalogue_id  # Associate the product with the catalogue
        )
        serializer = CatalogueProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CatalogueProduct Retrieve, Update, and Delete API
class CatalogueProductRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return CatalogueProduct.objects.get(pk=pk)
        except CatalogueProduct.DoesNotExist:
            return None

    def get(self, request, pk):
        catalogue_product = self.get_object(pk)
        if catalogue_product:
            serializer = CatalogueProductSerializer(catalogue_product)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        catalogue_product = self.get_object(pk)
        if catalogue_product:
            serializer = CatalogueProductSerializer(
                catalogue_product, data=request.data
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        catalogue_product = self.get_object(pk)
        if catalogue_product:
            catalogue_product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
