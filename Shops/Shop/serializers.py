
from rest_framework import serializers
from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
    distance = serializers.FloatField(read_only=True)

    class Meta:
        model = Shop
        fields = ['name', 'latitude', 'longitude', 'owner', 'distance']
