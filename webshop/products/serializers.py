from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from products.models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'price', 'description']



