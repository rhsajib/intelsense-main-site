from rest_framework.generics import ListAPIView
from .models import Blog
from .serializers import BlogSerializer

class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class FeaturedBlogListAPIView(ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        featured = self.kwargs['featured']
        return Blog.objects.filter(featured=featured)
