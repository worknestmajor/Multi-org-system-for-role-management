from django.contrib.auth.models import AbstractUser
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    ORGANIZATION_ROLES = [
        ('ADMIN', 'Admin'),
        ('VIEWER', 'Viewer'),
    ]

    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="users", null=True, blank=True
    )
    role = models.CharField(
        max_length=10, choices=ORGANIZATION_ROLES, default='VIEWER'
    )

    def __str__(self):
        return self.username
