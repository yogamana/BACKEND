from . import models
#import models
from rest_framework import serializers


class Memberserializers(serializers.ModelSerializer):
    
    class meta:
        model = models.Member
        exclude = ['profile_image']

