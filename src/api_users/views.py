from django.contrib.auth.models import auth
from django.shortcuts import redirect
from rest_framework.authentication import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView

from middlewares.jwt import generate_token
from .serializers import AuthCustomTokenSerializer, UserSerializer


class Login(ObtainAuthToken):
    serializer_class = AuthCustomTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            data = generate_token(user)
            return data


class CreateUser(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            instance.set_password(instance.password)
            instance.save()
            user = authenticate(email=instance.email, password=request.data.get('password'))
            data = generate_token(user)
            return data


def logout(request):
    auth.logout(request)
    return redirect('/')
