from django.shortcuts import render
from .serializers import UserRegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# from django.contrib.auth.models import User

# Create your views here.

class Registerview(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class Protectedview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({"message":"You have access to this view"})
    
class Logoutview(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message":"Logged out successfully"})
        except Exception as e:
            return Response({"error":str(e)})

