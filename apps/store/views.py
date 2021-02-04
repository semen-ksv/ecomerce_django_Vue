from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions, status

from apps.store.models import Product, Category
from apps.store.serializers import ProductSerializer, CategorySerializer


class ProductListView(ListAPIView):
    """
     """
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailView(RetrieveAPIView):
    """
     """

    serializer_class = ProductSerializer
    lookup_field = 'slug'
    queryset = Product.objects.all()

class CategoryListView(ListAPIView):
    """
     """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetailView(APIView):
    """
     """

    def get(self, request, slug):
        products_list = Product.objects.filter(category__slug=slug)
        return Response(data=ProductSerializer(products_list, many=True).data)