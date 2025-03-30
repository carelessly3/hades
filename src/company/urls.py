from django.urls import path
from company.api.company import (
    CompanyListCreateAPIView,
    CompanyRetrieveUpdateDestroyAPIView,
    CompanyProfileUpdateAPIView,
)

urlpatterns = [
    # Company endpoints
    path("/", CompanyListCreateAPIView.as_view(), name="company-list-create"),
    path(
        "/<int:pk>/",
        CompanyRetrieveUpdateDestroyAPIView.as_view(),
        name="company-retrieve-update-destroy",
    ),
    # Company Profile endpoints
    path(
        "/<int:pk>/profile/",
        CompanyProfileUpdateAPIView.as_view(),
        name="company-profile-update",
    ),
]
