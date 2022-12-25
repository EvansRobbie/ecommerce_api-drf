from django.urls import path
from .views import productApis, ProductApi,category_apis, category_api

urlpatterns = [
    path('products/', view=productApis),
    path('products/<str:pk>/', view = ProductApi),
    path('categories/', view=category_apis),
    path('categories/<str:pk>/', view=category_api)
]