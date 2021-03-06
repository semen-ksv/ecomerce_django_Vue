"""ecomerce_dj_vue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('openapi', get_schema_view(
            title="Your Project",
            description="API for all things …",
            version="1.0.0"
        ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui/swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('core/', include('apps.core.urls', namespace='core')),
    path('store/', include('apps.store.urls', namespace='store')),
    path('cart/', include('apps.cart.urls', namespace='cart')),
    path('auth/', include('apps.users.urls', namespace='users')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
