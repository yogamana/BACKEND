from urllib import request
from .permissions import IsSuperuser
from django.shortcuts import render, HttpResponse 
from django.contrib.auth.models import User
from . import models
from . import serializers
from rest_framework import generics


# Create your views here.
class MemberListGenerics(generics.ListCreateAPIView):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializers


class MemberDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializers
    lookup_field = 'pk'
    permission_classes = (IsSuperuser,)


class UserListGenerics(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers
    permission_classes = (IsSuperuser,)

    
class UserDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers
    lookup_field = 'pk'
    permission_classes = (IsSuperuser,)
