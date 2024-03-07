# Generated by Django 5.0.2 on 2024-03-06 03:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("branches", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Finance",
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
                ("last_modified", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=15, verbose_name="Amount"
                    ),
                ),
                (
                    "received_from",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Received From",
                    ),
                ),
                (
                    "paid_to",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Paid To"
                    ),
                ),
                (
                    "receipt_number",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Receipt Number",
                    ),
                ),
                (
                    "receipt_screenshot",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Receipt Screenshot",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("income", "Income"),
                            ("expense", "Expense"),
                            ("investment", "Investment"),
                            ("withdrawal", "Withdrawal"),
                        ],
                        max_length=20,
                        verbose_name="Type",
                    ),
                ),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="branches.branch",
                        verbose_name="Branch",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created By",
                    ),
                ),
            ],
            options={
                "verbose_name": "Finance",
                "verbose_name_plural": "Finances",
            },
        ),
    ]
