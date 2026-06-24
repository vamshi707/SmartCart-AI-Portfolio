from django.db import models


class HardwareSpec(models.Model):

    # COMMON PRODUCT INFO

    name = models.CharField(max_length=200)

    category = models.CharField(max_length=100)

    brand = models.CharField(max_length=100)

    image = models.URLField()

    price = models.IntegerField()

    stock = models.IntegerField()

    material = models.CharField(max_length=100)

    description = models.TextField()

    # FLEXIBLE PRODUCT DATA

    specifications = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name