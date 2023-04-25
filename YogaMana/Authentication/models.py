from re import T
from django.db import models


# Create your models here.
class Membership(models.Model):
    membership_id = models.IntegerField(unique=True)
    member_id = models.IntegerField()
    membership_title = models.TextField(max_length=250)
    

class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(unique=True,max_length=200)
    password = models.CharField(unique=True,max_length=200)
    email = models.EmailField(max_length=20,unique=True)
    #membership = models.ForeignKey(models.Membershi, verbose_name=_(""), on_delete=models.CASCADE)
    created_date = models.DateField()
    #profile_image = models.ImageField()


    



    