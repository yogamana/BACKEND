from dataclasses import field, fields
from . import models
from django.contrib.auth.models import User
from rest_framework import serializers


class MemberSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Member
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'


class PhysicalInfoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.PhysicalInfo
        fields = '__all__'


class CourseSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Course
        fields = '__all__'


class AddressSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Address
        fields = '__all__'


class ProgramSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Program
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Category
        fields = '__all__'


class CourseVideoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.CourseVideo
        fields = '__all__'


class PurchaseSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Purchase
        fields = '__all__'


class MembershipSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Membership
        fields = '__all__'
