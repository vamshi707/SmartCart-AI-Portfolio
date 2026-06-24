from django.urls import path
from .views import send_otp, register_user, verify_login_otp

urlpatterns = [
    path('send-otp/', send_otp),
    path('register/', register_user),
    path('verify-login-otp/', verify_login_otp),
]