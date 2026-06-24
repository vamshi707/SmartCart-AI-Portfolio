from django.urls import path
from .views import place_order, my_orders,cancel_product,admin_orders,delete_order

urlpatterns = [
    path("place-order/", place_order),
    path("my-orders/", my_orders),
    path(
    "cancel-product/<int:id>/",
    cancel_product
                    ),
    path(
    "admin-orders/",
    admin_orders
),

    path(
    "delete-order/<int:id>/",
    delete_order
),
]