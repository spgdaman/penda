from django.shortcuts import render
from callcenter.models import CallLogs

from .serializer import Callserializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class Calls(ListCreateAPIView):
    queryset = CallLogs.objects.all()
    serializer_class = Callserializer
