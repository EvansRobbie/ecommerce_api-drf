from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .Serializers import ProductSerializer, CategorySerializer, ReviewSerializer, CartSerializer,CartItemsSerializer,AddCartItemsSerializer,UpdateCartitemsSerializer
from storeapp.models import Product, Category, Review, Cart,Cartitems
# Filtering
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilterSet
# Search
from rest_framework.filters import SearchFilter,OrderingFilter
# Pagination
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class ProductViewSets(ModelViewSet):
    queryset  = Product.objects.all()
    serializer_class  = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    # filterset_fields = ['category_id']
    filterset_class = ProductFilterSet
    # search
    search_fields = ['name', 'description']
    # ordering
    ordering_fields = ['old_price']
    # pagination
    pagination_class = PageNumberPagination
    """
        Whenever we have similar classes like this, we can opt to use viewsets, Not a must but one cans use them.
        when using viewsets, we use routers
    """
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
        
# class ApiProduct(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSelializer

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



class CategoryViewSet(ModelViewSet):
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

# class ApiCategory(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
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

class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

class CartViewSet(CreateModelMixin, RetrieveModelMixin,DestroyModelMixin, GenericViewSet):
    queryset =  Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(ModelViewSet):
    # to avoid conflicts between the put and the patch you cal list out the required trrps methods
    http_method_names = ['get', 'post', 'patch', 'delete']
    # queryset = Cartitems.objects.all()---gets all items of every cart in general
    # Use querry set function to to get item of a specic cart - fetch item for only a given cart
    def get_queryset(self):
        return Cartitems.objects.filter(cart_id = self.kwargs['cart_pk'])
    # serializer_class = CartItemsSerializer
    # get self to add a product to the item
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemsSerializer
        
        # to update a particular field in the model we use PATCH
        elif self.request.method == 'PATCH':
            return UpdateCartitemsSerializer

        return  CartItemsSerializer

    # use get_serializer_context to get the specific cart id
    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}



        



