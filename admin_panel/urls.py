from . import views
from django.urls import path, include
from .api import router

urlpatterns = [
    path('', views.users_panel, name='users'),
    path('groups_list/', views.group_panel, name='groups'),
    path('api/', include(router.urls)),
    path('group', views.users_panel, name='groups'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_group/', views.add_group, name='add_group'),
    path('user_edit/<int:user_id>', views.user_edit, name='user_edit'),
    path('group_edit/<int:group_id>', views.group_edit, name='group_edit'),
]
