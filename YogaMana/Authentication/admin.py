from django.contrib import admin 
from .models import Membership
from .models import Member
from .models import Course
from .models import Program
from .models import CourseVideo
from .models import PhysicalInfo
from .models import Purchase
from .models import Category
from .models import Address
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
# @admin.register(Member)
# class MemberAdmin(admin.ModelAdmin):
#    list_display = ['user_name', 'password', 'created_date']


class CustomMemberAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
            ('Profile', {'fields': (
                                'member_id',
                                #'first_name',
                                #'last_name',
                                #'username',
                                #'password',
                                'phone_number',
                                #'email',
                                #'created_date',
                                'profile_image',
            )}),
    )


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'price', 'length', 'rating']


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'program_id']


class MembershipAdmin(admin.ModelAdmin):
    list_display = ['membership_title', 'member_id', 'membership_id']


class CourseVideoAdmin(admin.ModelAdmin):
    list_display = ['video_id', 'course_id', 'category_id', 'video_title', 'length']


class PhysicalInfoAdmin(admin.ModelAdmin):
    list_display = ['physical_info_id', 'member_id', 'height', 'weight', 'gender', 'birth_date']


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['purchase_id', 'member_id', 'course_id', 'payment_status']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_title']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['address_id', 'member_id', 'country', 'city', 'address_phone']


admin.site.register(Course, CourseAdmin)
admin.site.register(Member, CustomMemberAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(CourseVideo, CourseVideoAdmin)
admin.site.register(PhysicalInfo, PhysicalInfoAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Address, AddressAdmin)
# admin.site.register(get_user_model(), CustomUserAdmin)
