
from django.urls import path, include

from apps.users.views import login

app_name = 'users'

urlpatterns = [
    # path('login/', ProductListView.as_view()),
    # path('register/', ProductDetailView.as_view()),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken'))

]
