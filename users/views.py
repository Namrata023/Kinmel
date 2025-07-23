from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView

from rest_framework.response import Response
from .serializers import RegisterSerializer,UserProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework import status
from utils.response import success_response
User = get_user_model()
from utils.exceptions import custom_exception_handler


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return success_response("Profile retrieved successfully", data=serializer.data)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return success_response("Profile updated successfully", data=response.data)
class UserHomeView(APIView):
    def get(self, request):
        return success_response({"message": "Welcome to the users Home."})
    
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        print("Registering user with data:", request.data)
        context = {'request': request}
        try:
            print("Registering user with data:", request.data)
            response = super().create(request, *args, **kwargs)
            return success_response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error during registration: {e}")
            return custom_exception_handler(e, context)
