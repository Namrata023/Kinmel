from django.urls import path, include
from .views import  OrderListCreateView, OrderDetailView



urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]