# Generated by Django 4.1.7 on 2023-02-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resellers', '0009_alter_job_refferal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='refferal_code',
            field=models.CharField(default='fa275', max_length=255, unique=True),
        ),
    ]
