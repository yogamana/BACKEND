from urllib import request
from Authentication.permissions import IsSuperuser
from django.shortcuts import render, HttpResponse 
from django.contrib.auth.models import User
from . import models
from . import serializers
from rest_framework import generics


# Create your views here.
class MemberListgenerics(generics.ListCreateAPIView):
    queryset = models.Member.objects.all()
    serializer_class = serializers.Memberserializers
    
class MemberDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Member.objects.all()
    serializer_class = serializers.Memberserializers
    lookup_field ='pk'
    permission_classes = (IsSuperuser ,)
    
    

class UserListgenerics(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.Userserializers
    permission_classes = (IsSuperuser ,)

    
class UserDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.Userserializers
    lookup_field ='pk'
    permission_classes = (IsSuperuser,)
    


