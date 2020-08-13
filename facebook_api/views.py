from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics,permissions
from .serializers import *
from .models import *
from rest_framework import status
from django.contrib.auth import login,logout
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.
class LoginView(APIView):
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
        login(request,user)
        return Response({'detail':'Logout Done'},status=status.HTTP_200_OK)


class RegisterAPIView(generics.CreateAPIView):
     permission_classes=(permissions.AllowAny,)
     serializer_class=RegisterSerializer
     queryset= User.objects.all()
     model = User

     def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        check_data = {'username': username,'password': password,'email': email,'first_name': first_name,'last_name': last_name,}
        serializer = RegisterSerializer(data=check_data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
