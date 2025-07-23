from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Favorite, Product
from .serializers import FavoriteSerializer,ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import pandas as pd
from .recommend import get_similar_products


class FavoriteListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavoriteDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'product_id'

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET'])
def recommended_products(request, product_id):
    products = Product.objects.all().values('id', 'name', 'description', 'tags', 'category')
    df = pd.DataFrame(products)

    if product_id not in df['id'].values:
        return Response({'error': 'Product not found'}, status=404)

    recommended_ids = get_similar_products(product_id, df)
    recommended_items = Product.objects.filter(id__in=recommended_ids)
    serializer = ProductSerializer(recommended_items, many=True)
    return Response(serializer.data)