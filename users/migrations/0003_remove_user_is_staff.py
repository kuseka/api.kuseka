# Generated by Django 4.1.7 on 2023-03-02 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]