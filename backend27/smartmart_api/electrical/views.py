from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HardwareSpec
from .serializers import HardwareSerializer
from .detect import detect_hardware_ai
from PIL import Image
import base64
from io import BytesIO
# GET PRODUCTS + ADD PRODUCTS
@api_view(['GET', 'POST'])
def hardware_products(request):
    # GET PRODUCTS
    if request.method == 'GET':
        products = HardwareSpec.objects.all()
        serializer = HardwareSerializer(
            products,
            many=True
        )
        return Response(serializer.data)
    # ADD PRODUCT
    elif request.method == 'POST':
        serializer = HardwareSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
# DELETE PRODUCT
@api_view(['DELETE'])
def delete_hardware(request, id):
    product = HardwareSpec.objects.get(id=id)
    product.delete()
    return Response({
        "message": "Hardware Deleted"
    })
# AI HARDWARE DETECTION

@api_view(['POST'])
def detect_hardware(request):

    # GET IMAGE + CATEGORY

    image_data = request.data.get("image")

    selected_category = request.data.get("category")

    # SPLIT BASE64 IMAGE

    format, imgstr = image_data.split(';base64,')

    # CONVERT IMAGE

    image_file = BytesIO(
        base64.b64decode(imgstr)
    )

    image = Image.open(image_file)

    # FIX PNG/JPG

    image = image.convert("RGB")

    # SAVE TEMP IMAGE

    image_path = "temp_detect_image.jpg"

    image.save(image_path)

    # RUN AI

    ai_result = detect_hardware_ai(
        image_path
    )

    detected_category = ai_result["category"]

    confidence = ai_result["confidence"]

    length_mm = ai_result["length_mm"]

    diameter_mm = ai_result["diameter_mm"]

    # GET PRODUCTS BY CATEGORY

    matched_products = HardwareSpec.objects.filter(

        category__icontains=selected_category

    )

    # FILTER PRODUCTS MANUALLY

   

    filtered_products = []

    for product in matched_products:

        try:

            product_length = int(
                product.specifications.get(
                    "length_mm",
                    0
                )
            )

            product_diameter = int(
                product.specifications.get(
                    "diameter_mm",
                    0
                )
            )

            print("PRODUCT:", product.name)

            # SCREW FILTER
            if selected_category.lower() == "screw":

                if length_mm <= product_length <= length_mm + 5:

                    filtered_products.append(product)
            

            # PIPE FILTER
            elif selected_category.lower() == "pipe":

                    pipe_diameter = int(
                        product.specifications.get(
                            "diameter",
                            0
                        )
                    )

                    if length_mm <= pipe_diameter <= length_mm + 5:

                        filtered_products.append(product)


            # BOLT FILTER
            elif selected_category.lower() == "bolt":


                 if length_mm <= product_length <= length_mm + 5:

                    filtered_products.append(product)

            # OTHER PRODUCTS
            else:

                filtered_products.append(product)

        except Exception as e:

            print("FILTER ERROR:", e)

    # SERIALIZER

    serializer = HardwareSerializer(

        filtered_products,

        many=True

    )

    # RETURN RESPONSE

    return Response({

        "category": selected_category,

        "confidence": confidence,

        "length_mm": length_mm,

        "diameter_mm": diameter_mm,

        "output_image": ai_result["output_image"],

        "products": serializer.data

    })