# Generated by Django 4.1.7 on 2023-02-25 20:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transactions', '0001_initial'),
        ('vendors', '0001_initial'),
        ('resellers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingResource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('resellers_requested', models.IntegerField()),
                ('resellers_experince', models.IntegerField()),
                ('resellers_average_rating', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('industry', models.TextField()),
                ('commissions', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_draft', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=False)),
                ('estimated_reach', models.DecimalField(decimal_places=2, max_digits=10)),
                ('jobs', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='campaign_jobs', to='resellers.job')),
                ('softwares', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='software', to='vendors.software')),
                ('training_resources', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='training_resources', to='campaigns.trainingresource')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transaction', to='transactions.transaction')),
            ],
        ),
    ]
