from rest_framework.serializers import ModelSerializer
from rest_framework import fields, serializers
from products.models import Product, ProductPhoto

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'price', 'description', 'created']

class ProductPhotoSerializer(ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['link', 'pictures']


