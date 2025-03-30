from django.db import models
from hades.helpers.models import BaseModel


# only keep essential company details here.
class Company(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# all this data is optional technically.
class CompanyProfile(BaseModel):
    company = models.OneToOneField(
        Company, on_delete=models.CASCADE, related_name="profile"
    )
    address = models.TextField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)  # not sure how to handle this rn
    description = models.TextField(blank=True, null=True)
    certifications = models.TextField(
        blank=True, null=True
    )  # JSON or comma-separated list
    carbon_footprint_details = models.TextField(blank=True, null=True)
    manufacturing_capacity = models.TextField(blank=True, null=True)
    moq_policy = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    social_media_links = models.JSONField(
        blank=True, null=True
    )  # Store social media links as JSON
    established_year = models.IntegerField(blank=True, null=True)
    number_of_employees = models.IntegerField(blank=True, null=True)
    annual_revenue = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    quality_standards = models.TextField(
        blank=True, null=True
    )  # E.g., ISO, GOTS, OEKO-TEX

    def __str__(self):
        return f"Profile of {self.company.name}"
