from rest_framework import serializers
from .models import HardwareSpec


class HardwareSerializer(serializers.ModelSerializer):

    class Meta:
        model = HardwareSpec
        fields = '__all__'