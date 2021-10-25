
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action, api_view



class ProductSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductSetPagination
    permission_classes = [AllowAny]
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


