# Generated by Django 4.2.6 on 2023-10-23 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_alter_group_users_alter_user_group'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='group',
            table='groups',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
