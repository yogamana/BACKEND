from django.contrib import admin 
from .models import Membership
from .models import Member
from .models import Course
from .models import Program


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'password', 'created_date']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'price', 'length', 'rating']


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'program_id']


class MembershipAdmin(admin.ModelAdmin):
    list_display = ['membership_title', 'member_id', 'membership_id']


admin.site.register(Course, CourseAdmin)
# admin.site.register(Member)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Membership, MembershipAdmin)
