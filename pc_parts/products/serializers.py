from rest_framework import serializers

from .models import Product, Brand, Category

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
   
    class Meta:

        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'brand',
            'category'
        ]

class BrandSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()   
    products = ProductSerializer(read_only=True, many=True)
    class Meta:
        model = Brand
        depth = 1
        fields = [
            'id',
            'name',
            'products'
        ]

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
   
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]