from django.shortcuts import render
from rest_framework import APIView
from rest_framework import generics,permissions
from .serializers import *
from .models import *
from rest_framework import status
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.
class LoginView(APIview):
    permission_classes = [AllowAny,]
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data["user"]
        return Response({'user_id': user.id}, status=status.HTTP_200_OK)
