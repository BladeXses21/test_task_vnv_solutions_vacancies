from django.shortcuts import render, redirect

from .models import User, Group
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer


# Create your views here.
def users_panel(request):
    users = User.objects.all()
    return render(request, 'users.html', {"users": users})


def group_panel(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {"groups": groups})


def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        is_admin = request.POST.get('is_admin', False)

        # Створюємо нового користувача у базі даних
        User.objects.create(username=username, is_admin=is_admin)

        return redirect('users')  # Повертаємо користувача на сторінку зі списком користувачів

    return render(request, 'add_user.html')


def add_group(request):
    if request.method == 'POST':
        name = request.POST['name']
        data_analytics = request.POST.get('data_analytics', False)
        services_analytics = request.POST.get('services_analytics', False)
        voice_analytics = request.POST.get('voice_analytics', False)
        queue_stats = request.POST.get('queue_stats', False)
        voice_stats = request.POST.get('voice_stats', False)
        video = request.POST.get('video', False)
        smart_access = request.POST.get('smart_access', False)
        diagram = request.POST.get('diagram', False)

        Group.objects.create(name=name, data_analytics=data_analytics, services_analytics=services_analytics, voice_analytics=voice_analytics,
                             queue_stats=queue_stats, voice_stats=voice_stats, video=video, smart_access=smart_access, diagram=diagram)

        return redirect('users')

    return render(request, 'add_group.html')


def user_edit(request, user_id: int):
    user = User.objects.get(id=user_id)
    groups = Group.objects.all()
    return render(request, 'user_edit.html', {"user": user, 'groups': groups})


def group_edit(request, group_id: int):
    group = Group.objects.get(id=group_id)
    users = User.objects.all()
    return render(request, 'group_edit.html', {"group": group, 'users': users})


class CanUpdateUserGroupPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]

    def get_permissions(self):
        if self.action == 'update':
            return [CanUpdateUserGroupPermission()]
        return [permissions.IsAuthenticated()]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_permissions(self):
        if self.action == 'update':
            return [CanUpdateUserGroupPermission()]
        return [permissions.IsAuthenticated()]
