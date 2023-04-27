from dataclasses import field, fields
from . import models
#import models
from rest_framework import serializers


class Memberserializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Member
        #field = ['first_name','last_name' ,'user_name','password','email','created_date']
        fields = '__all__'
        #exclude = ['profile_image']

