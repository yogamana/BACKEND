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


admin.site.register(Course, CourseAdmin)
#admin.site.register(Member)
admin.site.register(Program)
admin.site.register(Membership)
