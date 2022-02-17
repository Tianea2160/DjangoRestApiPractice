from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Profile, Family
from rest_framework.authtoken.models import Token

# Create your views here.

class SignupView(APIView):
    def post(self, request):
        user = User.objects.create_user(request.data["id"], password=request.data['password]'])
        profile = Profile(user=user, nickname=request.data['nickname'])

        user.save()
        profile.save()

        Token.objects.create(user=user)
        







