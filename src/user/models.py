from django.db import models
from hades.helpers.models import BaseModel
from django.contrib.auth.models import AbstractUser

# Create your models here.


# create a base abstract user model.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ("company_admin", "Company Admin"),
        ("company_lead", "Company Lead"),
        ("registered_lead", "Registered Lead"),
        ("anonymous_lead", "Anonymous Lead"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey(
        "company.Company", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return f"{self.user.username} ({self.role})"
