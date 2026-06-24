from django.db import models

class GroceryProduct(models.Model):

    name = models.CharField(max_length=200)

    image = models.URLField(max_length=1000)

    price = models.IntegerField()

    old_price = models.IntegerField()

    discount = models.CharField(max_length=100)

    weight = models.CharField(max_length=100)

    rating = models.FloatField()

    rating_count = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Groceries_grocery'
