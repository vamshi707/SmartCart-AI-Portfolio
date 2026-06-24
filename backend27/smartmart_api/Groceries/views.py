from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import GroceryProduct
from .serializers import GrocerySerializer

# ADD THESE IMPORTS
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
import json


@api_view(['GET', 'POST'])
def grocery_products(request):

    if request.method == 'GET':

        products = GroceryProduct.objects.all()

        serializer = GrocerySerializer(
            products,
            many=True,
            context={'request': request}
        )

        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = GrocerySerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        print(serializer.errors)

        return Response(serializer.errors)


@api_view(['DELETE'])
def delete_product(request, id):

    product = GroceryProduct.objects.get(id=id)

    product.delete()

    return Response("Product Deleted")


# CHECK EMAIL API

@api_view(['POST'])
def check_email(request):

    email = request.data.get("email")

    exists = User.objects.filter(
        email=email
    ).exists()

    return Response({
        "exists": exists
    })


# LOGIN API

@api_view(['POST'])
def login_user(request):

    email = request.data.get("email")
    password = request.data.get("password")

    user = User.objects.filter(
        email=email
    ).first()

    if user:

        auth_user = authenticate(
            username=user.username,
            password=password
        )

        if auth_user:

            return Response({
                "message": "Login Success"
            })

    return Response({
        "message": "Wrong Password"
    }, status=400)


# REGISTER API

@api_view(['POST'])
def register_user(request):

    name = request.data.get("name")
    email = request.data.get("email")
    password = request.data.get("password")

    User.objects.create_user(
        username=email,
        email=email,
        password=password,
        first_name=name
    )

    return Response({
        "message": "Registered Successfully"
    })