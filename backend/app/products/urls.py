from django.urls import path
from .views import ProductListAPIView, TopProductListAPIView, ProductDetailAPIView

app_name = 'products'

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('<uuid:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('top/', TopProductListAPIView.as_view(), name='top-product-list'),
]
