from re import T
from django.db import models
from django.contrib.auth.models import User 


# Create your models here.
class Membership(models.Model):
    membership_id = models.IntegerField(unique=True)
    member_id = models.IntegerField()
    membership_title = models.TextField(max_length=250)
    

class Member(models.Model):
    # id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(unique=True, max_length=200)
    password = models.CharField(unique=True, max_length=200)
    # user = models.OneToOneField(u'id',User , on_delete=models.CASCADE , null=True)
    #phone = models.CharField(max_length=11, default='+98')
    email = models.EmailField(unique=True)
    #membership = models.models.OneToOneField(Membership, verbose_name=_(""),
    # on_delete=models.CASCADE)(models.Membership, verbose_name=_(""), on_delete=models.CASCADE)
    created_date = models.DateField()
    #profile_image = models.ImageField()


class Address(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.TextField(max_length=300)
    phone = models.CharField(max_length=13)


class Course(models.Model):
    course_id = models.IntegerField()
    category_id = models.IntegerField()
    course_title = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    course_image = models.ImageField()
    length = models.CharField()
    reting = models.FloatField()
    price = models.IntegerField()
    membership_acsess = models.BigAutoField()


class Program(models.Model):
    program_id = models.IntegerField()
    course_id = models.IntegerField()
    description = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
