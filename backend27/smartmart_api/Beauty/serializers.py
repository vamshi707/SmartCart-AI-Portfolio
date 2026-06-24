from rest_framework import serializers
from .models import BeautyProduct

class BeautyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeautyProduct
        fields = "__all__"