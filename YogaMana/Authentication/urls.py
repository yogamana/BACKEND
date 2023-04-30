from django.contrib import admin
from django.urls import path
from . import views
#app_name='Authentication'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path("memberList/", views.MemberListgenerics.as_view() , name='members_list_info'),
    path("member/<int:pk>/", views.MemberDetailGeneric.as_view() , name='member_detail_info'),
    path("userList/", views.UserListgenerics.as_view() , name='user_list_info'),
    path("user/<int:pk>/", views.UserDetailGeneric.as_view() , name='users_detail_info'),
]
