# from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# app_name='Authentication'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("memberList/", views.MemberListGenerics.as_view(), name='members_list_info'),
    path("member/<int:pk>/", views.MemberDetailGeneric.as_view(), name='member_detail_info'),
    path("userList/", views.UserListGenerics.as_view(), name='user_list_info'),
    path("user/<int:pk>/", views.UserDetailGeneric.as_view(), name='users_detail_info'),
    path('api-auth/', include('rest_framework.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
