# Generated by Django 5.0.2 on 2024-03-14 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0005_alter_clientlimit_client"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="guarantor",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="self"
            ),
        ),
    ]