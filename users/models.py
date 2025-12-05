# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('client', 'Client (NutriConnect User)'),
        ('farmer', 'Farmer'),
        ('ngo', 'NGO Representative'),
        ('marketplace', 'Marketplace Admin'),
    )
    role = models.CharField(max_length=15, choices=USER_ROLES, default='client')

    def __str__(self):
        return f"{self.username} ({self.role})"


# Supporting models for dashboards
class Order(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'client'})
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.status})"


class Crop(models.Model):
    farmer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'farmer'})
    name = models.CharField(max_length=100)
    quantity = models.FloatField()  # in kg

    def __str__(self):
        return f"{self.name} - {self.quantity}kg"


class Project(models.Model):
    ngo = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'ngo'})
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Ongoing')

    def __str__(self):
        return f"{self.name} ({self.status})"


class Donation(models.Model):
    ngo = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'ngo'})
    donor = models.CharField(max_length=100)
    amount = models.FloatField()

    def __str__(self):
        return f"{self.donor} - {self.amount}"
