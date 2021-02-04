
from django.urls import path

from apps.core.views import initial

app_name = 'core'

urlpatterns = [
    path('', initial),
]
