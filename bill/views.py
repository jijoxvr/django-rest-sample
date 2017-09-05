from django.shortcuts import render
from rest_framework import viewsets
from .models import Bill
from .serializer import BillModelSerializer

class BillModelViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillModelSerializer

# Create your views here.
