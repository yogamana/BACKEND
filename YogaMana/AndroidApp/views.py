from urllib import request
from .permissions import IsSuperuser
from django.shortcuts import render, HttpResponse 
from django.contrib.auth.models import User
from . import models
from . import serializers
from rest_framework import generics
# from rest_framework.authentication import BasicAuthentication
# Create your views here.


class MemberListGenerics(generics.ListCreateAPIView):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializers
    permission_classes = (IsSuperuser,)


class MemberDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializers
    lookup_field = 'pk'
    permission_classes = (IsSuperuser,)
    
class PysicalInfoDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PhysicalInfo.objects.all()
    serializer_class = serializers.Pysical_info_Serializers
    lookup_field = 'pk'
    permission_classes = (IsSuperuser,)

class CourseListGeneric(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.course_Serializers
    permission_classes = (IsSuperuser,)

class CourseDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.course_Serializers
    lookup_field = 'pk'
    permission_classes = (IsSuperuser,)

class AddressDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.Address_Serializers
    lookup_field = 'pk'
    permission_classes = (IsSuperuser,)

class ProgramDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Program.objects.all()
    serializer_class = serializers.Program_Serializers
    lookup_field = 'pk'
    permission_classes = (IsSuperuser,)


class CategoryDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.Category_Serializers
    lookup_field = 'pk'
    permission_classes = (IsSuperuser,)

class CategoryListGeneric(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.Category_Serializers
    permission_classes = (IsSuperuser,)

class CourseVideoDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CourseVideo.objects.all()
    serializer_class = serializers.CourseVideo_Serializers
    lookup_field = 'pk'
    permission_classes = (IsSuperuser,)

class PurchaseListGeneric(generics.ListCreateAPIView):
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.Purchase_Serializers
    permission_classes = (IsSuperuser,)


class PurchaseDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.Purchase_Serializers
    lookup_field = 'pk'
    permission_classes = (IsSuperuser,)

class MembershipDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Membership.objects.all()
    serializer_class = serializers.Membership_Serializers
    lookup_field = 'pk'
    permission_classes = (IsSuperuser,)






"""
class UserListGenerics(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers
    permission_classes = (IsSuperuser,)


class UserDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers
    lookup_field = 'pk'
    permission_classes = (IsSuperuser,)
"""