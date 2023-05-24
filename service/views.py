from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from service.models import User
from service.permissions import PermissionPolicyMixin
from service.serializer import UserSerializers


class UserViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes_per_method = {
        'list': [IsAdminUser, IsAuthenticated],
        'create': [AllowAny],
        'update': [IsAdminUser, IsAuthenticated],
        'destroy': [IsAdminUser],
        'retrieve': [IsAdminUser]
    }


def index(request):
    return render(request, "index.html")


def register(request):
    return render(request, "register.html")
