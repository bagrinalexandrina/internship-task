from rest_framework.serializers import ModelSerializer
from rest_framework import fields, serializers
from products.models import Product, ProductImage

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'price', 'description', 'created']

class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['link', 'product_image']


