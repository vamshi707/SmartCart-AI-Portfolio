from django.urls import path

from .views import detect_furniture

from .views import (
    furniture_products,
    delete_furniture
)

urlpatterns = [

    path(
        'furniture/',
        furniture_products
    ),

    path(
        'furniture/delete/<int:id>/',
        delete_furniture
    ),

    path(
    "detect-furniture/",
    detect_furniture
),

]