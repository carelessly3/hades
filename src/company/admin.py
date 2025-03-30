from django.contrib import admin
from .models import Company, CompanyProfile


# Register the Company model
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at", "updated_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")

    # Add fieldsets for better organization in the admin panel
    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "description",
                    "logo_url",
                    "email",
                    "phone",
                    "address",
                )
            },
        ),
        (
            "Additional Information",
            {
                "fields": (
                    "website",
                    "social_media_links",
                    "established_year",
                    "number_of_employees",
                    "annual_revenue",
                    "quality_standards",
                )
            },
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )


# Register the CompanyProfile model
@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "certifications",
        "carbon_footprint_details",
        "manufacturing_capacity",
        "moq_policy",
    )
    search_fields = ("company__name", "certifications")
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")

    # Add fieldsets for better organization in the admin panel
    fieldsets = (
        ("Company", {"fields": ("company",)}),
        (
            "Profile Details",
            {
                "fields": (
                    "certifications",
                    "carbon_footprint_details",
                    "manufacturing_capacity",
                    "moq_policy",
                )
            },
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
