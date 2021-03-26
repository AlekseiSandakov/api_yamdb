from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from .views import UserViewSet


router_V1 = DefaultRouter()
router_V1.register(
    'users',
    UserViewSet,
    basename='users',
)

urlpatterns = [
    path('v1/', include(router_V1.urls)),
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]