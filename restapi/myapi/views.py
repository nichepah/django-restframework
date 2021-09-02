from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import CoilSerializer
from .models import Coil

class CoilViewSet(viewsets.ModelViewSet):
    queryset = Coil.objects.all().order_by('id')
    serializer_class = CoilSerializer
