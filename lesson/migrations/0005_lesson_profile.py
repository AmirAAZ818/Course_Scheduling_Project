# Generated by Django 4.1.4 on 2023-01-18 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_remove_profile_lessons'),
        ('lesson', '0004_remove_lesson_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_lessons', to='user_profile.profile'),
        ),
    ]
