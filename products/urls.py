
from django.urls import path, include
from .views import FavoriteListCreateView, FavoriteDeleteView, ProductListCreateView, ProductDetailView


urlpatterns = [
     path('favorites/', FavoriteListCreateView.as_view(), name='favorites'),
    path('favorites/<int:product_id>/', FavoriteDeleteView.as_view(), name='favorite'),
    path('product/', ProductListCreateView.as_view(), name='product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
