from django.contrib import admin 
from Authentication.models import Member, Membership
from Authentication.models import Member
# Register your models here.
from .models import Course
from .models import Program

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'password']


admin.site.register(Course)
