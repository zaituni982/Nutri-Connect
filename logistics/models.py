# logistics/models.py
from django.db import models
from users.models import CustomUser
from marketplace.models import FoodItem

class Order(models.Model):
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='purchases')

    limit_choices_to={'role__in': ['ngo', 'marketplace']}
    
    
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    payment_status = models.BooleanField(default=False)
    
    pickup_status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('picked', 'Picked'),
            ('delivered', 'Delivered'),
        ],
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.food_item.name}"
