# Generated by Django 4.1.7 on 2023-02-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resellers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='refferal_code',
            field=models.CharField(default='35187', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='resellerprofile',
            name='jobs',
            field=models.ManyToManyField(blank=True, related_name='jobs', to='resellers.job'),
        ),
    ]
