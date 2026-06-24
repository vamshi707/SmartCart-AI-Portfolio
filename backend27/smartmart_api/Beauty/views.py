from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BeautyProduct
from .serializers import BeautyProductSerializer

@api_view(["GET", "POST"])
def beauty_products(request):
    if request.method == "GET":
        products = BeautyProduct.objects.all()
        serializer = BeautyProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = BeautyProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(["DELETE"])
def delete_beauty_product(request, id):
    product = BeautyProduct.objects.get(id=id)
    product.delete()
    return Response({"message": "Beauty product deleted successfully"})