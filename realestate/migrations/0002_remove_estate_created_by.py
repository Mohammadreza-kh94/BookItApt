# Generated by Django 4.2 on 2023-04-15 09:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("realestate", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="estate",
            name="created_by",
        ),
    ]
