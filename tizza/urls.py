from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView

from pizza.routers import router as pizza_router

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Tizza API",
      default_version='v1',
      description="An App that consumes the daraja v2.0 endpoints and helps with Lipa-na-Mpesa function",
      terms_of_service="https://github.com/weshy007/django-daraja/blob/main/LICENCE",
      contact=openapi.Contact(email="josephwaweru96@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizzas/', include('pizza.urls')),

    path('user/', include('user.urls')),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('', include(pizza_router.urls)),

    path('api/v1', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
