from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions, status




@api_view(('GET',))
def initial(request):
    return Response(data={'name':"Hello word"})

# class StatisticListView(ListAPIView):
#     """
#      """
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [permissions.IsAuthenticated]