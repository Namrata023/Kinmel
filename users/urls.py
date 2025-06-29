from django.urls import path
from .views import *
from .serializers import RegisterSerializer
urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('home/', UserHomeView.as_view(), name='user-home'),
    path('register/', RegisterView.as_view(), name='register'),

]
