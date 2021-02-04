
from django.urls import path

from apps.store.views import ProductListView, ProductDetailView, CategoryListView, CategoryDetailView

app_name = 'store'

urlpatterns = [
    path('product/', ProductListView.as_view()),
    path('product/<str:slug>', ProductDetailView.as_view()),

    path('category/', CategoryListView.as_view()),
    path('category/<str:slug>', CategoryDetailView.as_view()),
]
