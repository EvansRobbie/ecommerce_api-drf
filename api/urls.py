from django.urls import path
from .views import ApiProducts, ApiProduct,ApiCategories, ApiCategory

urlpatterns = [
    path('products/', view=ApiProducts.as_view()),
    path('products/<str:pk>/', view = ApiProduct.as_view()),
    path('categories/', view=ApiCategories.as_view()),
    path('categories/<str:pk>/', view=ApiCategory.as_view())
]