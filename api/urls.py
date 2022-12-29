from django.urls import path,include
# from .views import ApiProducts, ApiProduct,ApiCategories, ApiCategory
from . import views
# from rest_framework.routers import DefaultRouter
# NEsted routers drf-nested-routers
from rest_framework_nested import routers

# parent Router
router = routers.DefaultRouter()
router.register('products', views.ProductViewSets)
router.register('categories', views.CategoryViewSet)
router.register('carts', views.CartViewSet)

# Child Router
# products/Product_pk/reviews/product_rweview_detail or product_reviews_list
product_router = routers.NestedDefaultRouter(router, 'products', lookup = 'product')
product_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

# Cart child Router
# cart/cart_ph/items/cart_detail
cartitem_router = routers.NestedDefaultRouter(router,'carts', lookup ='cart')
cartitem_router.register('items', views.CartItemViewSet, basename='cartitem_detail')


# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cartitem_router.urls))
    # path('products/', view=ApiProducts.as_view()),
    # path('products/<str:pk>/', view = ApiProduct.as_view()),
    # path('categories/', view=ApiCategories.as_view()),
    # path('categories/<str:pk>/', view=ApiCategory.as_view())
]