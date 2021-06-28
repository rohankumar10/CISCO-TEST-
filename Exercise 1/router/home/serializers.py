from rest_framework import serializers
from .models import Router

class RouterDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Router
        fields = ['id', 'host_name', 'sap_id', 'loopback_id', 'ipv4', 'mac_address']
