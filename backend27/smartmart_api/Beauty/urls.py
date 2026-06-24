from django.urls import path
from .views import beauty_products, delete_beauty_product

urlpatterns = [
    path("beauty/", beauty_products),
    path("beauty/delete/<int:id>/", delete_beauty_product),
]