# Generated by Django 4.1.7 on 2023-02-26 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resellers', '0002_alter_job_refferal_code_alter_resellerprofile_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='refferal_code',
            field=models.CharField(default='f7dbd', max_length=255, unique=True),
        ),
    ]
