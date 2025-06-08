
from django.urls import path, include
from .views import FavoriteListCreateView, FavoriteDeleteView


urlpatterns = [
     path('favorites/', FavoriteListCreateView.as_view(), name='favorites'),
    path('favorites/<int:product_id>/', FavoriteDeleteView.as_view(), name='favorite-delete'),
]
