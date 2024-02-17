# Generated by Django 5.0.2 on 2024-02-17 02:39

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("clients", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="NextOfKin",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "first_name",
                    models.CharField(max_length=50, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Last Name"),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=128,
                        null=True,
                        region=None,
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "relationship",
                    models.CharField(max_length=255, verbose_name="Relationship"),
                ),
                ("address", models.TextField(verbose_name="Address")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="next_of_kin",
                        to="clients.client",
                        verbose_name="Client",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created By",
                    ),
                ),
            ],
            options={
                "verbose_name": "Next of Kin",
                "verbose_name_plural": "Next of Kin",
            },
        ),
    ]
