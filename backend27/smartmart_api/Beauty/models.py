from django.db import models



class BeautyProduct(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.URLField(max_length=1000)
    price = models.IntegerField()
    old_price = models.IntegerField()
    stock = models.IntegerField()
    rating = models.FloatField()
    skin_type = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    shade = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name