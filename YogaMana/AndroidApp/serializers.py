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

class Pysical_info_Serializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.PhysicalInfo
        fields = '__all__'

class course_Serializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Course
        fields = '__all__'
        
class Address_Serializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Address
        fields = '__all__'


class Program_Serializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Program
        fields = '__all__'

class Category_Serializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Category
        fields = '__all__'

class CourseVideo_Serializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.CourseVideo
        fields = '__all__'

class Purchase_Serializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Purchase
        fields = '__all__'

class Membership_Serializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Membership
        fields = '__all__'
