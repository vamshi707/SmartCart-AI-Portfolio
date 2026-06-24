from django.db import models
from django.db import models

class Order(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    total_amount = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )
    product_name = models.CharField(max_length=200)
    product_image = models.URLField(max_length=1000)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
# Create your models here.

    cancelled = models.BooleanField(
        default=False
    )

    cancel_reason = models.CharField(
        max_length=200,
        blank=True
    )
