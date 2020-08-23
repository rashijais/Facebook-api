from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,permissions
from .serializers import *
from .models import *
from rest_framework import status
from django.contrib.auth import login,logout
from django.contrib.auth import get_user_model
from rest_framework import viewsets
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
     model = User

     def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        check_data = {'username': username,'password': password,'email': email,}
        serializer = RegisterSerializer(data=check_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    #permission_classes = (permissions.IsAuthenticated)

    '''def perform_create(self, serializer):
        user_obj = self.request.user.username
        print(user_obj)
        serializer.save(user=self.request.user,name=user_obj)
    def get_queryset(self):
        if self.action == 'users_Post':
            return Post.objects.filter(user=self.request.user)
        else:
            return Post.objects.all()

    @action(methods=['GET',],detail=False)
    def users_Post(self,*args,**kwargs):
        list = Post.objects.filter(user = self.request.user)
        serializer = PostSerializer(list,many=True)
        return Response({'detail':serializer.data})'''
