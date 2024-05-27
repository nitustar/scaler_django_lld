from rest_framework import serializers
from ecomProject.models import Product, DairyProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class DairyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DairyProduct
        fields = '__all__'
