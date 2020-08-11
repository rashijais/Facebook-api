from django.shortcuts import render
from rest_framework import APIView
from rest_framework import generics,permissions
from .serializers import *
from .models import *
from rest_framework import status
from django.contrib.auth import login,logout
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.
class LoginView(APIview):
    permission_classes = [permissions.AllowAny,]
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data["user"]
        login(request,user)
        return Response({'user_id': user.id}, status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes=[permissions.AllowAny,]

    def get(self,request):
        login(request)
        return Response({'detail':'Logout Done'},status=status.HTTP_200_OK)
