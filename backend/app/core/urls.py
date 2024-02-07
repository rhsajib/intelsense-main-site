from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Intelsense API',
        default_version='v1',
        description='End to End Microservice Hub',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='contact@snippets.local'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/',
        include([
            path('about_us/', include('about_us.urls', namespace='about_us')),
            path('blogs/', include('blogs.urls', namespace='blogs')),
            path('career/', include('career.urls', namespace='career')),
            path('contact_us/', include('contact_us.urls', namespace='contact_us')),
            path('investors/', include('investors.urls', namespace='investors')),
            path('members/', include('members.urls', namespace='members')),
            path('partners/', include('partners.urls', namespace='partners')),
            path('products/', include('products.urls', namespace='products')),
            path('services/', include('services.urls', namespace='services')),
        ])
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
