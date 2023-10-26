from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, related_name='group_users', blank=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class Group(models.Model):
    name = models.CharField(max_length=20)
    users = models.ManyToManyField(User, related_name='user_groups', blank=True)
    data_analytics = models.BooleanField(default=False)
    services_analytics = models.BooleanField(default=False)
    voice_analytics = models.BooleanField(default=False)
    queue_stats = models.BooleanField(default=False)
    voice_stats = models.BooleanField(default=False)
    video = models.BooleanField(default=False)
    smart_access = models.BooleanField(default=False)
    diagram = models.BooleanField(default=False)

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return self.name
