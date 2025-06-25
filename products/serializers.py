from rest_framework import serializers
from .models import Favorite, Product, Category, ProductImage

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
   class Meta:
        model = Product
        fields = '__all__'