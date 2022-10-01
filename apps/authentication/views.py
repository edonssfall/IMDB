from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from .serializer import UserSerializer, RegisterSerializer

User = get_user_model()


class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class CurrentUserAPIView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        if not self.request.user.is_authenticated:
            raise Http404

        return self.request.user