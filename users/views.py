from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView

from rest_framework.response import Response
from .serializers import RegisterSerializer,UserProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework import status
User = get_user_model()


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
class UserHomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the users Home."})
    
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)