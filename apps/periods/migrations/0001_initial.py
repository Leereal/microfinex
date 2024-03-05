# Generated by Django 5.0.2 on 2024-03-05 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Period",
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
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                (
                    "duration",
                    models.IntegerField(
                        help_text="Duration of the period in units specified by 'Duration Unit'.",
                        verbose_name="Duration",
                    ),
                ),
                (
                    "duration_unit",
                    models.CharField(
                        choices=[
                            ("DAYS", "Days"),
                            ("WEEKS", "Weeks"),
                            ("MONTHS", "Months"),
                            ("YEARS", "Years"),
                        ],
                        default="MONTHS",
                        help_text="Unit of measurement for the period's duration.",
                        max_length=10,
                        verbose_name="Duration Unit",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
            ],
            options={
                "verbose_name": "Period",
                "verbose_name_plural": "Periods",
            },
        ),
    ]