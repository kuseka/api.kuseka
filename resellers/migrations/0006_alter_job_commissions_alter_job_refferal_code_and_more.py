# Generated by Django 4.1.7 on 2023-02-26 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0003_trainingresource'),
        ('resellers', '0005_alter_job_softwares'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='commissions',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='refferal_code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='softwares',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='softwares', to='utils.software'),
        ),
        migrations.AlterField(
            model_name='job',
            name='training_completion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='job',
            name='training_resources',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='courses', to='utils.trainingresource'),
        ),
    ]