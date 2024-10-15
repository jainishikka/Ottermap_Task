from django.shortcuts import render
from django.urls import path
from .views import register_shop
from .views import shop_search
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path('register/', register_shop, name='register_shop'),
    path('success/', lambda request: render(request, 'Shop/shop_success.html'), name='shop_success'),
    path('search/',shop_search,name='shop_search'),
]
