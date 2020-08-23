from django.urls import path,include
from .import views
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', views.PostView)

urlpatterns = [
    path('',include(router.urls)),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view()),
    path('register/', RegisterAPIView.as_view(), name='register'),
]
