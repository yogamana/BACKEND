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
