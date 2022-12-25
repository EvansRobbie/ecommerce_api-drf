from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .Serializers import ProductSelializer, CategorySerializer
from storeapp.models import Product, Category

# Create your views here.
@api_view(['POST', 'GET'])
def productApis(request):
    product = Product.objects.all()
    if request.method == 'GET':
        serializer = ProductSelializer(product, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ProductSelializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def ProductApi(request, pk):
    instance = get_object_or_404(Product, id = pk)
    if request.method == 'GET':
        # instance = Product.objects.get(id = pk)
        # use get_object_or_404 to display a readable error message if a product doesnt exist
        
        serializer = ProductSelializer(instance, many  =False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = ProductSelializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    if request.method == 'DELETE':
        instance.delete()
        return Response({'res': 'Product Deleted Succesfully'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def category_apis(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many = True)
        return Response (serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def category_api(request, pk):
    category = get_object_or_404(Category, category_id = pk)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = CategorySerializer(category, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        category.delete()
        return Response({'res': 'Category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



