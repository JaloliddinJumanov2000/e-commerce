from django.contrib import admin
from django.urls import path, include
from djoser import permissions
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view


class JWTSchemaGenerator(OpenAPISchemaGenerator):
    def get_security_definitions(self):
        security_definitions = super().get_security_definitions()
        security_definitions['Bearer'] = {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
        return security_definitions


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="E-commerce API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=JWTSchemaGenerator,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('products.urls')),
]
