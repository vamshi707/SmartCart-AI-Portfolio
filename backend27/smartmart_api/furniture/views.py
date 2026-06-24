from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Furniture
from .serializers import FurnitureSerializer

import base64
import os

from django.conf import settings
from .room_generator import generate_room


# GET ALL PRODUCTS + ADD PRODUCT

@api_view(['GET', 'POST'])
def furniture_products(request):

    if request.method == 'GET':

        products = Furniture.objects.all()

        serializer = FurnitureSerializer(
            products,
            many=True
        )

        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = FurnitureSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)


# DELETE PRODUCT

@api_view(['DELETE'])
def delete_furniture(request, id):

    product = Furniture.objects.get(id=id)

    product.delete()

    return Response("Furniture Deleted")

@api_view(['POST'])
def detect_furniture(request):

    room = request.data.get("room")
    image = request.data.get("image")

    if not room:

        return Response({
            "error": "Room required"
        })

    products = Furniture.objects.filter(
        category=room
    ).order_by("priority")

    image_path = None

    if image:

        if "," in image:

            format, imgstr = image.split(";base64,")

            image_data = base64.b64decode(imgstr)

            image_path = os.path.join(
                settings.MEDIA_ROOT,
                "uploaded_room.jpg"
            )

            with open(image_path, "wb") as f:

                f.write(image_data)

    generated_image = None

    if image_path:

        generated_image = generate_room(
            image_path,
            products
        )

    serializer = FurnitureSerializer(
        products,
        many=True
    )

    return Response({

        "products": serializer.data,

        "generated_image": generated_image,

        "room_type": room

    })