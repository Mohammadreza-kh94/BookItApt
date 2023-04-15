# Generated by Django 4.2 on 2023-04-14 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Estate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("sqft", models.IntegerField()),
                ("price", models.FloatField()),
                ("bedrooms", models.IntegerField()),
                ("bathrooms", models.IntegerField()),
                ("photo", models.ImageField(upload_to="img/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("message", models.TextField(blank=True)),
                ("check_in_date", models.DateField()),
                ("check_out_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "estate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="realestate.estate",
                    ),
                ),
            ],
        ),
    ]
