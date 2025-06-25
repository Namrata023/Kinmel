from django.urls import path, include
from .views import ShippingAddressListCreateView, ShippingAddressDetailView

urlpatterns = [
    path('shipping/', ShippingAddressListCreateView.as_view(), name='shipping-address-list-create'),
    path('shipping/<int:pk>/', ShippingAddressDetailView.as_view(), name='shipping-address-detail'),
]

