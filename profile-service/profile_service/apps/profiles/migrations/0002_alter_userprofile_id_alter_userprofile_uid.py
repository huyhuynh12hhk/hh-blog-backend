# Generated by Django 5.1.6 on 2025-02-24 01:43

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="uid",
            field=models.CharField(max_length=36, unique=True),
        ),
    ]
