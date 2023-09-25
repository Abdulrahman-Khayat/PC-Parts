import uuid
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product, Category, Brand
from products.serializers import ProductSerializer, BrandSerializer, CategorySerializer
import logging

logger = logging.getLogger(__name__)

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def list(self, request, *args, **kwargs):
        logger.info("GEcfgdfgdfgdfgdfgdfgT")
        return super().list(request, *args, **kwargs)

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()


class BrandListCreateAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

brand_list_create_view = BrandListCreateAPIView.as_view()


class BrandDetailAPIView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

brand_detail_view = BrandDetailAPIView.as_view()

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    paginator = None
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

category_list_create_view = CategoryListCreateAPIView.as_view()


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

category_detail_view = CategoryDetailAPIView.as_view()
