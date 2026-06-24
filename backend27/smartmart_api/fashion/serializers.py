from rest_framework import serializers

from .models import FashionProduct


class FashionSerializer(serializers.ModelSerializer):

    class Meta:
        model = FashionProduct
        fields = '__all__'