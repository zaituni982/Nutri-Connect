from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('farmer', 'Farmer'),
        ('marketplace', 'Marketplace'),
        ('ngo', 'NGO'),
        ('government', 'Government'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
