from django.urls import path
from .views import Calls

urlpatterns = [
    path('api/v1/calls/', Calls.as_view(), name = 'call_data')
]
