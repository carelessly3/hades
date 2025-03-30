from django.db import models

# Create your models here.


from django.db import models
from hades.helpers.models import BaseModel


class Inquiry(BaseModel):
    user = models.ForeignKey("user_management.Profile", on_delete=models.CASCADE)
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("responded", "Responded"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Inquiry from {self.user.user.username} to {self.company.name}"


class InquiryItem(BaseModel):
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in inquiry {self.inquiry.id}"
