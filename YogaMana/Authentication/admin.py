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
from .models import CourseMemberRelationships
from .models import CourseCategoryRelationships


class PurchasedCourseIdInline(admin.TabularInline):
    model = Course.members_access.through


class CourseCategoryIdInline(admin.TabularInline):
    model = Course.category_id.through


class CustomMemberAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': (
                                # 'member_id',
                                # 'first_name',
                                # 'last_name',
                                # 'username',
                                # 'password',
                                'phone_number',
                                # 'email',
                                # 'created_date',
                                'profile_image',
                                # 'get_purchased_course_id'
            )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': (
            'email',
        )}),
    )
    """
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Add Member', {'fields': (
                #'first_name',
                #'last_name',
                'Username',
                'Password',
                'Password confirmation',
                #'phone_number',
                'Email',
                #'profile_image',
          )}),
    )
    #"""


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'price', 'length', 'rating']
    inlines = (PurchasedCourseIdInline, CourseCategoryIdInline,)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'date_start', 'date_end']


class MembershipAdmin(admin.ModelAdmin):
    list_display = ['membership_title', 'member_id']


class CourseVideoAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'category_id', 'video_title', 'length']


class PhysicalInfoAdmin(admin.ModelAdmin):
    list_display = ['member_id', 'height', 'weight', 'gender', 'birth_date']


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['member_id', 'course_id', 'payment_status']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['member_id', 'country', 'city', 'address_phone']


class CourseMemberRelationshipsAdmin(admin.ModelAdmin):
    list_display = ['member', 'course', 'validate']


class CourseCategoryRelationshipsAdmin(admin.ModelAdmin):
    list_display = ['category', 'course', 'validate']


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
admin.site.register(CourseMemberRelationships, CourseMemberRelationshipsAdmin)
admin.site.register(CourseCategoryRelationships, CourseCategoryRelationshipsAdmin)
