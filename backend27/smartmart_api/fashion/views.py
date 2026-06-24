from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FashionProduct
from .serializers import FashionSerializer

# GET ALL PRODUCTS + ADD PRODUCT

@api_view(['GET', 'POST'])
def fashion_products(request):

    if request.method == 'GET':

        products = FashionProduct.objects.all()

        serializer = FashionSerializer(products, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = FashionSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)


# DELETE PRODUCT

@api_view(['DELETE'])
def delete_product(request, id):

    product = FashionProduct.objects.get(id=id)

    product.delete()

    return Response("Product Deleted")


# AI DETECT FASHION

@api_view(['POST'])
def detect_fashion(request):

    try:

        import base64
        import numpy as np

        from PIL import Image
        from io import BytesIO

        image_data = request.data.get("image")

        if not image_data:

            return Response({
                "error": "No image received"
            }, status=400)

        # BASE64 SPLIT

        format, imgstr = image_data.split(';base64,')

        # IMAGE CONVERT

        image = Image.open(
            BytesIO(base64.b64decode(imgstr))
        ).convert("RGB")

        image_np = np.array(image)

        height, width, channels = image_np.shape

        center_face = image_np[
            height//3:height//2,
            width//3:width//2
        ]

        avg_color = center_face.mean(axis=(0, 1))

        brightness = avg_color.mean()

        # TONE DETECTION

        if brightness < 110:

            tone = "dark"

        elif brightness < 180:

            tone = "medium"

        else:

            tone = "white"

        category = request.data.get("category")

        gender = request.data.get("gender")

        print("Tone:", tone)
        print("Gender:", gender)
        print("Category:", category)

        # PRODUCT FILTER

        products = FashionProduct.objects.filter(
            skin_type=tone,
            gender=gender,
            name__icontains=category
        )

        serializer = FashionSerializer(
            products,
            many=True
        )

        return Response({

            "skin_tone": tone,

            "products": serializer.data

        })

    except Exception as e:

        print("DETECT ERROR:", str(e))

        return Response({
            "error": str(e)
        }, status=500)