# Generated by Django 4.1.7 on 2023-02-26 14:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_software'),
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
    ]