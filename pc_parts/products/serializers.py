from rest_framework import serializers

from .models import Product, Brand, Category

class BrandSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()   
    # products = ProductSerializer(read_only=True, many=True)
    class Meta:
        model = Brand
        depth = 1
        fields = [
            'id',
            'name',
            # 'products'
        ]
        
class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
   
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    brand = BrandSerializer(read_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), write_only=True)
    category = CategorySerializer(read_only=True)  
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)

    class Meta:

        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'brand',
            'brand_id',
            'category',
            'category_id'
        ]
    def create(self, validated_data):
        validated_data['brand_id'] = validated_data['brand_id'].id
        validated_data['category_id'] = validated_data['category_id'].id

        obj = Product.objects.create(**validated_data)
        obj.save()
        return obj
