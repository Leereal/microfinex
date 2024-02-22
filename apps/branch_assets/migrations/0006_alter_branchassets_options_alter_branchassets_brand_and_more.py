# Generated by Django 5.0.2 on 2024-02-22 15:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "branch_assets",
            "0005_alter_branchassets_brand_alter_branchassets_color_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="branchassets",
            options={"verbose_name": "branch", "verbose_name_plural": "branches"},
        ),
        migrations.AlterField(
            model_name="branchassets",
            name="brand",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="brand",
            ),
        ),
        migrations.AlterField(
            model_name="branchassets",
            name="description",
            field=models.TextField(
                blank=True, default=None, null=True, verbose_name="description"
            ),
        ),
        migrations.AlterField(
            model_name="branchassets",
            name="images",
            field=models.JSONField(
                blank=True, default=list, null=True, verbose_name="images"
            ),
        ),
        migrations.AlterField(
            model_name="branchassets",
            name="item",
            field=models.CharField(
                max_length=255,
                validators=[django.core.validators.MinLengthValidator(3)],
                verbose_name="item",
            ),
        ),
        migrations.AlterField(
            model_name="branchassets",
            name="purchase_date",
            field=models.DateField(blank=True, null=True, verbose_name="purchase date"),
        ),
        migrations.AlterField(
            model_name="branchassets",
            name="quantity",
            field=models.IntegerField(default=1, verbose_name="quantity"),
        ),
    ]
