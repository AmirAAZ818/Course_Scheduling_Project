# Generated by Django 4.1.4 on 2022-12-31 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_alter_profile_lessons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='test',
        ),
    ]
