from django.shortcuts import render
from .serializers import MyTokenObtainPairSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrStaffOrReadOnly

from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthorOrStaffOrReadOnly, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly]
    lookup_field = 'username'
