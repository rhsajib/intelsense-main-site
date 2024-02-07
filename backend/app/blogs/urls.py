from django.urls import path
from .views import BlogListAPIView, FeaturedBlogListAPIView


app_name = 'blogs'

urlpatterns = [
    path('', BlogListAPIView.as_view(), name='blog-list'),
    path('featured/<str:featured>/', FeaturedBlogListAPIView.as_view(), name='featured-blog-list'),
]
