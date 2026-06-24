from django.db import models


class FashionProduct(models.Model):

    name = models.CharField(max_length=200)

    brand = models.CharField(max_length=100)

    description = models.TextField()

    image = models.URLField()

    price = models.IntegerField()

    old_price = models.IntegerField()

    rating = models.FloatField()

    skin_type = models.CharField(max_length=100)

    stock = models.IntegerField()

    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name