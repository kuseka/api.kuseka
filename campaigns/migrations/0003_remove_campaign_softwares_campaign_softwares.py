# Generated by Django 4.1.7 on 2023-02-26 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
        ('campaigns', '0002_alter_campaign_jobs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='softwares',
        ),
        migrations.AddField(
            model_name='campaign',
            name='softwares',
            field=models.ManyToManyField(blank=True, related_name='campaign_softwares', to='utils.software'),
        ),
    ]
