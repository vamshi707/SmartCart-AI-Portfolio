from rest_framework import serializers
from .models import GroceryProduct


class GrocerySerializer(serializers.ModelSerializer):

    class Meta:
        model = GroceryProduct
        fields = '__all__'