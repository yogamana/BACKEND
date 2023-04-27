from urllib import request
from django.shortcuts import render, HttpResponse 

#from django.contrib.auth.models import User
from . import models
from . import serializers
from rest_framework import generics


# Create your views here.
class UserListgenerics(generics.ListCreateAPIView):
    queryset = models.Member.objects.all()
    serializer_class = serializers.Memberserializers
    #templates_name = 'templates/Authentication/userInfo.html'
