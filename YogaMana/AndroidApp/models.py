from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model


class Member(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, default='+980000000000')
    email = models.EmailField(unique=True)
    created_date = models.DateField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='images/profile/', default='default.jpg')
    # REQUIRED_FIELDS = ['member_id', 'password', 'email']

    class Meta:
        verbose_name = "Member"
        # ordering = ('-member-id',)

    def __str__(self):
        return self.username


class Membership(models.Model):
    member_id = models.OneToOneField(Member, on_delete=models.CASCADE)
    membership_title = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.membership_title}"


class PhysicalInfo(models.Model):
    gender_choices = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('non', 'Not Preferred'),
    )
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    height = models.FloatField(validators=[MaxValueValidator(220)])
    weight = models.FloatField(validators=[MaxValueValidator(200)])
    birth_date = models.DateField()
    gender = models.CharField(max_length=20, choices=gender_choices, default='non')

    def __str__(self):
        return f"{self.member_id} --> {self.height} --> {self.weight} --> {self.gender}"


class Address(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.TextField(max_length=300)
    address_phone = models.CharField(max_length=13, default='+982100000000')

    def __str__(self):
        return f"{self.member_id} --> {self.country} --> {self.city}"


class Category(models.Model):
    category_title = models.CharField(max_length=200)

    def __str__(self):
        return self.category_title


class Course(models.Model):
    course_title = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    course_cover_image = models.ImageField(upload_to='images/course_cover/', default='default.jpg')
    length = models.DurationField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    price = models.CharField(max_length=15)
    members_access = models.ManyToManyField(Member, related_name='purchased_course_id',
                                            symmetrical=False, through='CourseMemberRelationships')
    category_id = models.ManyToManyField(Category, related_name='course_based_category',
                                         symmetrical=False, through='CourseCategoryRelationships', blank=True)

    class Meta:
        db_table = 'Category_Course_category_id'

    def __str__(self):
        return f"{self.course_title} "


class Program(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()


class CourseVideo(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=100)
    description = models.TextField()
    length = models.DurationField()
    video_file = models.FileField(upload_to='videos/', default='default.mp4')

    def __str__(self):
        return self.video_title


class Purchase(models.Model):
    payment_status_choices = (
        ('successful', 'Successful'),
        ('unsuccessful', 'Unsuccessful'),
        ('suspended', 'Suspended'),
    )
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    place_at = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20, choices=payment_status_choices, default='unsuccessful')

    def __str__(self):
        return f"{self.member_id} --> {self.course_id} --> {self.payment_status}"


class CourseMemberRelationships(models.Model):
    member = models.ForeignKey(get_user_model(), verbose_name='member', on_delete=models.CASCADE,
                               related_name='member2course')
    course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE,
                               related_name='course2member')
    validate = models.BooleanField(verbose_name='is valid?')

    class Meta:
        verbose_name = "CourseMemberRelationships"
        unique_together = ('member', 'course')

    def __str__(self):
        return f"{self.member.__str__()} -> {self.course.course_title} {'(validate)' if self.validate else ''}"


class CourseCategoryRelationships(models.Model):
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE,
                                 related_name='category_id')
    course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE,
                               related_name='course_based_category')
    validate = models.BooleanField(verbose_name='is valid?')

    class Meta:
        verbose_name = "CourseCategoryRelationships"
        unique_together = ('category', 'course')

    def __str__(self):
        return f"{self.category.category_title} -> {self.course.course_title} {'(validate)' if self.validate else ''}"
