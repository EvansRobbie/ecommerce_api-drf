from rest_framework.serializers import ModelSerializer
from storeapp.models import Product, Category

class ProductSelializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description' ,'slug','inventory','old_price','price','category']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields= ['category_id','title', 'slug']