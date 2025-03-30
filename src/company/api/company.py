from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from company.models import Company, CompanyProfile
from company.serializers import CompanySerializer, CompanyProfileSerializer


# Company List and Create API
class CompanyListCreateAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Company Retrieve, Update, and Delete API
class CompanyRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return None

    def get(self, request, pk):
        company = self.get_object(pk)
        if company:
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        company = self.get_object(pk)
        if company:
            serializer = CompanySerializer(company, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        company = self.get_object(pk)
        if company:
            company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


# Company Profile Update API
class CompanyProfileUpdateAPIView(APIView):
    def get_object(self, pk):
        try:
            return CompanyProfile.objects.get(company_id=pk)
        except CompanyProfile.DoesNotExist:
            return None

    def get(self, request, pk):
        profile = self.get_object(pk)
        if profile:
            serializer = CompanyProfileSerializer(profile)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        profile = self.get_object(pk)
        if profile:
            serializer = CompanyProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
