from django.db import models

class Furniture(models.Model):

    CATEGORY_CHOICES = [
        ('Bedroom', 'Bedroom'),
        ('Living Room', 'Living Room'),
        ('Office', 'Office'),
        ('Kitchen', 'Kitchen'),
    ]

    POSITION_CHOICES = [
        ('Left', 'Left'),
        ('Right', 'Right'),
        ('Center', 'Center'),
        ('Corner', 'Corner'),
        ('Front', 'Front'),
        ('Back', 'Back'),
        ('Wall', 'Wall'),
    ]

    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    position = models.CharField(
        max_length=20,
        choices=POSITION_CHOICES,
        default='Center'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.URLField()

    description = models.TextField(
        blank=True
    )

    stock = models.IntegerField(
        default=0
    )

    priority = models.IntegerField(
        default=1
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
