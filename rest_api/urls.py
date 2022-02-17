from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from . import views
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("signup/", views.SignupView.as_view()),
    path("users/", views.UserListView.as_view()),
    path("profiles/",views.ProfileListView.as_view()),
]