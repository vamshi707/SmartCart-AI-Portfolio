from django.test import TestCase

import random
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from twilio.rest import Client

from .models import User


TWILIO_ACCOUNT_SID = "your_sid"
TWILIO_AUTH_TOKEN = "your_token"
TWILIO_PHONE_NUMBER = "+1234567890"


@api_view(["POST"])
def send_otp(request):
    mobile = request.data.get("mobile")

    if not mobile:
        return Response({"error": "Mobile number required"}, status=400)

    otp = str(random.randint(100000, 999999))

    cache.set(f"otp_{mobile}", otp, timeout=300)

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=f"Your SmartMart OTP is {otp}",
        from_=TWILIO_PHONE_NUMBER,
        to=f"+91{mobile}"
    )

    existing_user = User.objects.filter(mobile=mobile).exists()

    return Response({
        "message": "OTP sent successfully",
        "existing_user": existing_user
    })


@api_view(["POST"])
def verify_login_otp(request):
    mobile = request.data.get("mobile")
    otp = request.data.get("otp")

    saved_otp = cache.get(f"otp_{mobile}")

    if saved_otp != otp:
        return Response({"error": "Invalid OTP"}, status=400)

    cache.delete(f"otp_{mobile}")

    return Response({"message": "Login successful"})


@api_view(["POST"])
def register(request):
    name = request.data.get("name")
    mobile = request.data.get("mobile")
    otp = request.data.get("otp")

    saved_otp = cache.get(f"otp_{mobile}")

    if saved_otp != otp:
        return Response({"error": "Invalid OTP"}, status=400)

    user, created = User.objects.get_or_create(
        mobile=mobile,
        defaults={"name": name}
    )

    cache.delete(f"otp_{mobile}")

    return Response({
        "message": "Registration successful",
        "user_id": user.id
    })