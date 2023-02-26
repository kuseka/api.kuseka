# Generated by Django 4.1.7 on 2023-02-26 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_alter_campaign_amount_alter_campaign_jobs_and_more'),
        ('resellers', '0005_alter_job_softwares'),
        ('utils', '0002_software'),
        ('vendors', '0002_remove_vendorprofile_phone_number_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Software',
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='campaigns',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='campaigns', to='campaigns.campaign'),
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='softwares',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vendor_softwares', to='utils.software'),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='vendor_email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='vendor_phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
