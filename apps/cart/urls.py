
from django.urls import path

from apps.cart.views import CartDetailView

app_name = 'cart'

urlpatterns = [
    path('', CartDetailView.as_view()),
]
