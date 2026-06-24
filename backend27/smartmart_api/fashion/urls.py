from django.urls import path

from .views import (
    fashion_products,
    delete_product,
    detect_fashion
)

urlpatterns = [

    path('fashion/', fashion_products),

    path('fashion/delete/<int:id>/', delete_product),

    path('detect-fashion/', detect_fashion),

]
