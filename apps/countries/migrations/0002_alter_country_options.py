# Generated by Django 5.0.2 on 2024-02-17 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("countries", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="country",
            options={"verbose_name": "country", "verbose_name_plural": "countries"},
        ),
    ]
