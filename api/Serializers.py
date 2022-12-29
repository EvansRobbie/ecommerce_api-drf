from rest_framework import serializers
from storeapp.models import Product, Category, Review, Cart, Cartitems, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= ['category_id','title', 'slug']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image']

class ProductSerializer(serializers.ModelSerializer):
    # add multiple images
    images = ProductImageSerializer(many = True, read_only = True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000,allow_empty_file = False,use_url = False), write_only = True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description' 
            ,'slug',
            # 'get_imageUrl',
            'inventory','old_price',
            'price',
            'category',
            'images', 
            'uploaded_images'
        ]
    # Serialization Relationship
    # Method one outputs the category name only
     # category = serializers.StringRelatedField()
    # Method 2 tooutput category as an object
    category = CategorySerializer()
    
    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        product = Product.objects.create(**validated_data)
        for image in uploaded_images:
            new_product_image = ProductImage.objects.create(product = product, image = image)

        return product

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date_created', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id = product_id, **validated_data)
class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name','price']


class CartItemsSerializer(serializers.ModelSerializer):
    subTotal = serializers.SerializerMethodField(method_name='Total')
    class Meta:
        model = Cartitems
        fields = ['id', 'product', 'quantity','subTotal']
    # product = serializers.StringRelatedField()
    product  = SimpleProductSerializer(many = False)
    def Total(self, cartitem:Cartitems):
        total = cartitem.quantity * cartitem.product.price
        return total

class AddCartItemsSerializer(serializers.ModelSerializer):
    product_id = serializers.UUIDField()
    # give a friendly error if the plroduct_id doesn't exist:
    def validate_product_id(self, value):
        if not Product.objects.filter(pk =  value).exists():
            raise serializers.ValidationError('There is no error with the given ID')

        return value

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            cartItem = Cartitems.objects.get(product_id = product_id, cart_id = cart_id)
            cartItem.quantity += quantity
            cartItem.save()

            self.instance = cartItem
        except:
           self.instance = Cartitems.objects.create(cart_id = cart_id, **self.validated_data) #
        
        return self.instance

    class Meta:
        model = Cartitems
        fields = ['id', 'product_id', 'quantity']
class UpdateCartitemsSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Cartitems
        fields = [ 'quantity']



class CartSerializer(serializers.ModelSerializer):
    id =  serializers.UUIDField(read_only = True)
    grand_total = serializers.SerializerMethodField(method_name='main_total')
    items = CartItemsSerializer(many = True, read_only = True)
    class Meta:
        model = Cart
        fields = ['id','items', 'grand_total']

    def main_total(self, cart: Cart):
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total




