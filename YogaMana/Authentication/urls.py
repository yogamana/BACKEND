from django.contrib import admin
from django.urls import path
from . import views
#app_name='Authentication'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path("userList/", views.UserListgenerics.as_view() , name='user_info'),
]
