from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer


@api_view(["POST"])
def place_order(request):
    try:
        print("ORDER DATA =", request.data)

        data = request.data

        order = Order.objects.create(
            email=data.get("email", ""),
            full_name=data.get("fullName", ""),
            phone=data.get("phone", ""),
            address=data.get("address", ""),
            total_amount=data.get("totalAmount", 0),
            payment_method=data.get("paymentMethod", ""),
        )

        for item in data.get("items", []):
            print("ITEM RECEIVED =", item)

            OrderItem.objects.create(
                order=order,
                product_name=item.get("name", ""),
                product_image=item.get("image", ""),
                price=int(float(item.get("price", 0))),
                quantity=int(item.get("quantity", 1)),
                category=item.get("category", "")
            )

        return Response({
            "message": "Order placed successfully"
        })

    except Exception as e:
        print("FURNITURE ERROR =", str(e))

        return Response({
            "error": str(e)
        }, status=500)


@api_view(["GET"])
def my_orders(request):
    email = request.GET.get("email")

    orders = Order.objects.filter(
        email=email
    ).order_by("-created_at")

    serializer = OrderSerializer(
        orders,
        many=True
    )

    return Response(serializer.data)

@api_view(["POST"])
def cancel_product(request, id):

    item = OrderItem.objects.get(id=id)

    item.cancelled = True

    item.cancel_reason = request.data.get(
        "reason",
        ""
    )

    item.save()

    return Response({
        "message": "Product Cancelled"
    })

@api_view(["GET"])
def admin_orders(request):

    orders = Order.objects.all().order_by("-created_at")

    serializer = OrderSerializer(
        orders,
        many=True
    )

    return Response(serializer.data)

@api_view(["POST"])
def delete_order(request, id):

    order = Order.objects.get(id=id)

    order.delete()

    return Response({
        "message": "Order deleted"
    })