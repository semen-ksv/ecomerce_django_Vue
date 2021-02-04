from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions, status


from apps.store.serializers import ProductSerializer, CategorySerializer


class CartDetailView(APIView):
    """
     """
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    serializer_class = ProductSerializer
    # queryset = Cart.objects.all()