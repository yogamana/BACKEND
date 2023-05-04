from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
#app_name='Authentication'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path("member-list/", views.MemberListgenerics.as_view() , name='members_list_info'),
    path("member/<int:pk>/", views.MemberDetailGeneric.as_view() , name='member_detail_info'),
    path("user-list/", views.UserListgenerics.as_view() , name='user_list_info'),
    path("user/<int:pk>/", views.UserDetailGeneric.as_view() , name='users_detail_info'),
    path("api-token-auth/",obtain_auth_token),
    
]
