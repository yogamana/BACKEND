from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Member(models.Model):
    member_id = models.IntegerField(primary_key=True, unique=True, default=-1)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, default='+980000000000')
    email = models.EmailField(unique=True)
    created_date = models.DateField()
    profile_image = models.ImageField(upload_to='images/profile/', default='default.jpg')


class Membership(models.Model):
    membership_id = models.IntegerField(primary_key=True, unique=True)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    membership_title = models.TextField(max_length=250)


class PhysicalInfo(models.Model):
    physical_info_id = models.IntegerField(primary_key=True, unique=True, default=-1)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    height = models.FloatField(validators=[MaxValueValidator(220)])
    weight = models.FloatField(validators=[MaxValueValidator(200)])
    birth_date = models.DateField()
    gender = models.CharField(max_length=13)


class Address(models.Model):
    address_id = models.IntegerField(primary_key=True, unique=True, default=-1)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.TextField(max_length=300)
    address_phone = models.CharField(max_length=13, default='+982100000000')


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True, unique=True, default=-1)
    course_title = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    course_cover_image = models.ImageField(upload_to='images/course_cover/', default='default.jpg')
    length = models.TimeField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    price = models.IntegerField()
    # members_access = models.ManyToManyField(Member)


class Program(models.Model):
    program_id = models.IntegerField(primary_key=True, unique=True, default=-1)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True, unique=True, default=-1)
    category_title = models.CharField(max_length=200)


class CourseVideo(models.Model):
    video_id = models.IntegerField(primary_key=True, unique=True, default=-1)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=100)
    description = models.TextField()
    length = models.TimeField()
    video_file = models.FileField(upload_to='videos/', default='default.mp4')


class Purchase(models.Model):
    payment_status_choices = (
        ('successful', 'Successful'),
        ('unsuccessful', 'Unsuccessful'),
        ('suspended', 'Suspended'),
    )
    purchase_id = models.IntegerField(primary_key=True, unique=True, default=-1)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    place_at = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20, choices=payment_status_choices, default='unsuccessful')


Member.purchased_course_id = models.ManyToManyField(Course)
Member.membership = models.OneToOneField(Membership, on_delete=models.CASCADE)
Course.category_id = models.ManyToManyField(Category)
