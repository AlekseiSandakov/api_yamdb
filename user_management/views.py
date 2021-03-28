from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.core.paginator import Paginator


from .permissions import IsAdmin
from .models import User, ConfirmationCode
from .serializers import MyTokenObtainPairSerializer, UserSerializer, UserConfirmCodeSerializer


class UserConfirmCodeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        confirmation_code = get_random_string(length=32)
        validatedData = serializer.validated_data
        user_email = validatedData.get('email')
        serializer.save(
            password=confirmation_code,
        )
        send_mail(
            'confirmation_code',
            confirmation_code,
            'from@example.com',
            [user_email],
            fail_silently=False,
        )


@api_view(['POST'])
@permission_classes([AllowAny])
def AuthTokenJwt(request):
    serializer = MyTokenObtainPairSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        confirmation_code = serializer.validated_data['confirmation_code']
        user = User.objects.get(
            email=email,
            password=confirmation_code
        )
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)
        return Response({'token': token})
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsAdmin, IsAuthenticated,)


class UserMeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_me'
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = User.objects.get(pk=self.request.user)
        return queryset
