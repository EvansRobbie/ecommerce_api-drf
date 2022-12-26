from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .Serializers import ProductSelializer, CategorySerializer
from storeapp.models import Product, Category

# Create your views here.

class ApiProducts(ListCreateAPIView):
    queryset  = Product.objects.all()
    serializer_class  = ProductSelializer
    # def get(self, request):
    #     product = Product.objects.all()
    #     serializer = ProductSelializer(product, many = True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # def post(self, request):
    #     serializer = ProductSelializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ApiProduct(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSelializer

    # def get(self, request, pk):
    #     instance = get_object_or_404(Product, id = pk)
    #     serializer = ProductSelializer(instance, many  =False)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request, pk):
    #     product = get_object_or_404(Product, id = pk)
    #     serializer = ProductSelializer(product , data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    # def delete(self,request, pk):
    #     product = get_object_or_404(Product, id = pk)
    #     product.delete()
    #     return Response({'res': 'Product Deleted Succesfully'}, status=status.HTTP_204_NO_CONTENT)



class ApiCategories(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # def get(self, request):
    #     category = Category.objects.all()
    #     serializer = CategorySerializer(category, many = True)
    #     return Response (serializer.data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     serializer = CategorySerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

class ApiCategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # def get(self, request,pk):
    #     category = get_object_or_404(Category, category_id = pk)
    #     serializer = CategorySerializer(category)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def put(self, request, pk):
    #     category = get_object_or_404(Category, category_id = pk)
    #     serializer = CategorySerializer(category, data= request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def delete(self, request, pk):
    #     category = get_object_or_404(Category, category_id = pk)
    #     category.delete()
    #     return Response({'res': 'Category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



        



