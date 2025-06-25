
from django.urls import path
from .views import CartItemListCreate, CartItemDetail

urlpatterns = [
    path('cart-items/', CartItemListCreate.as_view(), name='cart-item'),
    path('cart-items/<int:pk>/', CartItemDetail.as_view(), name='cartitem-detail'),
]
