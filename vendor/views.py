from django.shortcuts import render
from rest_framework import viewsets
from .models import Vendor
from .serializer import VendorModelSerializer

class VendorModelViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorModelSerializer

# Create your views here.
