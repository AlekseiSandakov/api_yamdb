from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    AuthTokenJwt,
    UserConfirmCodeViewSet,
    UserViewSet,
    UserMeViewSet,
)
router_v1 = DefaultRouter()
router_v1.register('auth/email', UserConfirmCodeViewSet)
router_v1.register('users/me', UserMeViewSet, basename='user_me')
router_v1.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('auth/token/', AuthTokenJwt),
    path('', include(router_v1.urls)),
]
