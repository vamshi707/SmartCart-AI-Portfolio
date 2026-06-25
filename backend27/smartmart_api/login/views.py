import random

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

otp_storage = {}


@api_view(["POST"])
def send_otp(request):
    email = request.data.get("email")

    if not email:
        return Response(
            {"message": "Email required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    otp = str(random.randint(1000, 9999))

    otp_storage[email] = otp

    try:
        send_mail(
            subject="SmartCart OTP",
            message=f"Your OTP is {otp}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
    except Exception as e:
        return Response(
            {
                "message": "Email sending failed",
                "error": str(e)
            },
            status=500
        )

    existing_user = User.objects.filter(email=email).exists()

    return Response({
        "message": "OTP sent",
        "existing_user": existing_user
    })


@api_view(["POST"])
def register_user(request):
    name = request.data.get("name")
    email = request.data.get("email")
    otp = request.data.get("otp")

    if otp_storage.get(email) != otp:
        return Response(
            {"message": "Invalid OTP"},
            status=400
        )

    if User.objects.filter(email=email).exists():
        return Response(
            {"message": "User already exists"},
            status=400
        )

    User.objects.create_user(
        username=email,
        first_name=name,
        email=email,
        password="defaultpassword123",
    )

    otp_storage.pop(email, None)

    return Response({
        "message": "Registration successful"
    })


@api_view(["POST"])
def verify_login_otp(request):
    email = request.data.get("email")
    otp = request.data.get("otp")

    if otp_storage.get(email) != otp:
        return Response(
            {"message": "Invalid OTP"},
            status=400
        )

    otp_storage.pop(email, None)

    return Response({
        "message": "Login successful"
    })