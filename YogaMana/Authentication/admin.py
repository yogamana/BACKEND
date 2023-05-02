from django.contrib import admin 
from Authentication.models import Member, Membership
from Authentication.models import Member
# Register your models here.


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'password']
