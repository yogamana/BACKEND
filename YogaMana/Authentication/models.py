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
    phone = models.CharField(max_length=11 , default='+98')
    email = models.EmailField(max_length=20,unique=True)
    #membership = models.models.OneToOneField(Membership, verbose_name=_(""), on_delete=models.CASCADE)(models.Membership, verbose_name=_(""), on_delete=models.CASCADE)
    created_date = models.DateField()
    profile_image = models.ImageField()
    
class Address(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.TextField(max_length=300)
    

    


    



    