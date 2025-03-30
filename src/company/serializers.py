from rest_framework import serializers
from .models import Company, CompanyProfile


class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at", "deleted_at")


class CompanySerializer(serializers.ModelSerializer):
    profile = CompanyProfileSerializer(read_only=True)  # Nested serializer for profile

    class Meta:
        model = Company
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at", "deleted_at")
