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

from django.contrib.auth import authenticate, login, logout


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
            
            response = super().create(request, *args, **kwargs)
            return success_response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error during registration: {e}")
            return custom_exception_handler(e, context)
        
class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        email = request.data.get('email') or request.POST.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {"error": "Email and password are required."},
            
            )
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Invalid email or password"}, status=401)

        user = authenticate(request, username=user_obj.username, password=password)
        if user:
            login(request, user)  
            return success_response(
                "Login successful",
                data={
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                }
            )
        else:
            return Response({"error": "Invalid email or password"}, status=401)
class LogoutView(APIView):
    permission_classes = []

    def post(self, request):
        if request.user.is_authenticated:
            logout(request)  # Clear session
            return success_response("Logout successful")
        else:
            return Response({"error": "You are not logged in"}, status=400)