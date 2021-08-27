from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from bills.serializers import *
from . import models
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView

class BillsViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
    permission_classes = [permissions.IsAuthenticated]