from django.urls import path

from .views import (

    hardware_products,

    delete_hardware,

    detect_hardware

)

urlpatterns = [

    path(

        'hardware/',

        hardware_products

    ),

    path(

        'hardware/delete/<int:id>/',

        delete_hardware

    ),

    path(

        'detect-hardware/',

        detect_hardware

    ),

]