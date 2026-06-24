from django.urls import path

from .views import *

urlpatterns = [

    path('grocery/', grocery_products),

    path('grocery/delete/<int:id>/', delete_product),

    path('check-email/', check_email),

    path('login/', login_user),

    path('register/', register_user),

]