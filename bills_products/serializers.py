from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class BillsProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillsProducts
        fields = '__all__'