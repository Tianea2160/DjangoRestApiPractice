import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from . import models
from .serializers import UserSerializer, ProfileSerializer
from rest_framework import status

from rest_framework import generics

class SignupView(APIView):
    def post(self, request):
        print(request.data)
        user = User.objects.create_user(username=request.data['id'], password=request.data['password'])
        profile = models.Profile(user=user, nickname=request.data['nickname'])

        user.save()
        profile.save()

        token = Token.objects.create(user=user)
        return Response({"Token": token.key})

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileListView(generics.ListAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer



