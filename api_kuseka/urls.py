"""api_kuseka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
   openapi.Info(
      title="Kuseka API",
      default_version='v1',
      description="This is the API for Kuseka and all its operations",
   ),
   public=True,
   authentication_classes=[],
   permission_classes=[AllowAny],

)


urlpatterns = [
    path('transactions/', include('transactions.urls')),
    path('auth/', include('users.urls')),
    path('vendor/', include('vendors.urls')),
    path('reseller/', include('resellers.urls')),
    path('billing/', include('billing.urls')),
    path('campaign/', include('campaigns.urls')),
    path('utils/', include('utils.urls')),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
