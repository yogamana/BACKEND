from django.contrib import admin
from django.urls import path
from . import views
#app_name='Authentication'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path("memberList/", views.MemberListgenerics.as_view() , name='members_list_info'),
    path("<int:pk>/", views.MemberDetailGeneric.as_view() , name='member_detail_info'),
]
