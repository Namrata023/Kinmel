from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserProfileSerializer
from rest_framework.response import Response

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
class UserHomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the users Home."})