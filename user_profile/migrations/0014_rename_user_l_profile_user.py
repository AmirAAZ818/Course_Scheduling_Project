# Generated by Django 4.1.4 on 2023-01-20 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0013_rename_user_profile_user_l'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_l',
            new_name='user',
        ),
    ]
