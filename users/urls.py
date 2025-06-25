from django.urls import path
from .views import *
urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('home/', UserHomeView.as_view(), name='user-home'),
]
