# from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# app_name='AndroidApp'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), #old version of authentication
    path("member-list/", views.MemberListGenerics.as_view() , name='members_list_info'), #list of member info
    path("cource-list/", views.CourseListGeneric.as_view() , name='courses_list_info'), #list of courses info
    path("category-list/", views.CategoryListGeneric.as_view() , name='category_list_info'), #list of category info
    path("purchase-list/", views.PurchaseListGeneric.as_view() , name='purchase_list_info'), #list of purchase info
    path("member/<int:pk>/", views.MemberDetailGeneric.as_view() , name='member_detail_info'), #detail info of a user in profile
    path("pysical-info/<int:pk>/", views.PysicalInfoDetailGeneric.as_view() , name='pysical_detail_info'), #detail pysycal info about a user
    path("course/<int:pk>/", views.CourseDetailGeneric.as_view() , name='course_detail_info'), #detail info of a course in profile
    path("address/<int:pk>/", views.AddressDetailGeneric.as_view() , name='address_detail_info'), #detail info of a address 
    path("program/<int:pk>/", views.ProgramDetailGeneric.as_view() , name='program_detail_info'), #detail info of a program 
    path("category/<int:pk>/", views.CategoryDetailGeneric.as_view() , name='category_detail_info'), #detail info of a category 
    path("course-video/<int:pk>/", views.CourseVideoDetailGeneric.as_view() , name='course_detail_info'), #detail info of a Course video 
    path("purchase/<int:pk>/", views.PurchaseDetailGeneric.as_view() , name='purchase_detail_info'), #detail info of a purchase 
    path('rest-auth/', include('dj_rest_auth.urls')), #new version of authentication
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')), #register a user
    # path("user-list/", views.UserListGenerics.as_view() , name='user_list_info'),
    # path("user/<int:pk>/", views.UserDetailGeneric.as_view() , name='users_detail_info'),
    # path("api-token-auth/",obtain_auth_token),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
