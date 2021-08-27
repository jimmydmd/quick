from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from products.serializers import *
from . import models
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]
    