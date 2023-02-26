# Generated by Django 4.1.7 on 2023-02-25 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resellers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resellerprofile',
            name='currency',
            field=models.TextField(choices=[('NGN', 'Nigeria Naira'), ('GHS', 'Ghana Cedi'), ('KSH', 'Kenya Shilling'), ('UGX', 'Uganda Shilling')], max_length=10),
        ),
        migrations.AlterField(
            model_name='resellerprofile',
            name='jobs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jobs', to='resellers.job'),
        ),
        migrations.AlterField(
            model_name='resellerprofile',
            name='ratings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ratings', to='resellers.rating'),
        ),
    ]