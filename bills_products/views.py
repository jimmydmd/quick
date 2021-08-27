from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from bills_products.serializers import *
from . import models
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView

class BillsProductsViewset(viewsets.ModelViewSet):
    queryset = BillsProducts.objects.all()
    serializer_class = BillsProductsSerializer
    permission_classes = [permissions.IsAuthenticated]


