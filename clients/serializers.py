from rest_framework import serializers
from .models import *

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'
