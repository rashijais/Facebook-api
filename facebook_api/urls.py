from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view()),
]
