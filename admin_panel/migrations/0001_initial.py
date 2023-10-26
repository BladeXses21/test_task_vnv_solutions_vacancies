# Generated by Django 4.2.6 on 2023-10-22 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('data_analytics', models.BooleanField(default=False)),
                ('services_analytics', models.BooleanField(default=False)),
                ('voice_analytics', models.BooleanField(default=False)),
                ('queue_stats', models.BooleanField(default=False)),
                ('voice_stats', models.BooleanField(default=False)),
                ('video', models.BooleanField(default=False)),
                ('smart_access', models.BooleanField(default=False)),
                ('diagram', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_users', to='admin_panel.group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(related_name='user_groups', to='admin_panel.user'),
        ),
    ]
