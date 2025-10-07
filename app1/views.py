from django.shortcuts import render
from .serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import ProductModel
from rest_framework import viewsets

@api_view(['POST'])
def add_product(request):
    product = ProductSerializer(data = request.data)

    if product.is_valid():
        product.save()
        return Response(product.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET'])
# def get_all_product(request):
#     products = ProductModel.objects.all()
#     product = ProductSerializer(products, many= True)
#     if product:
#         return Response(product.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['PATCH'])
# def update_product(request):
#     id = request.data.get('id')
    
#     try:
#         product = ProductModel.objects.get(id=id)
#     except:
#         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
#     serializer_class = ProductSerializer(product, data=request.data, partial=True)
#     if serializer_class.is_valid():
#         serializer_class.save()
#         return Response(serializer_class.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)




class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()