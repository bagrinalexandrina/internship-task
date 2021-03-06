from rest_framework.serializers import ModelSerializer
from rest_framework import fields, serializers
from products.models import Product, ProductPhoto

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'sku', 'price', 'description', 'created','images']

class ProductPhotoSerializer(ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['link', 'product']


