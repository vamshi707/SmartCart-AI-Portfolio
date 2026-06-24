from rest_framework import serializers

from .models import LoginDetail


class LoginSerializer(serializers.ModelSerializer):

    class Meta:

        model = LoginDetail

        fields = '__all__'