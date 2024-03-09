# Generated by Django 5.0.2 on 2024-03-08 17:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("branches", "0001_initial"),
        ("currencies", "0001_initial"),
        ("loan_transactions", "0001_initial"),
        ("loans", "0002_rename_repayment_date_loan_expected_repayment_date_and_more"),
        ("payment_gateways", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="loantransaction",
            name="loan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="loan_transactions",
                to="loans.loan",
                verbose_name="Loan",
            ),
        ),
        migrations.AlterField(
            model_name="loantransaction",
            name="transaction_type",
            field=models.CharField(
                choices=[
                    ("disbursement", "Disbursement"),
                    ("repayment", "Repayment"),
                    ("interest", "Interest"),
                    ("charge", "Charge"),
                    ("refund", "Refund"),
                    ("bonus", "bonus"),
                    ("topup", "Topup"),
                ],
                max_length=20,
                verbose_name="Transaction Type",
            ),
        ),
        migrations.AddConstraint(
            model_name="loantransaction",
            constraint=models.UniqueConstraint(
                condition=models.Q(("transaction_type", "disbursement")),
                fields=("loan",),
                name="unique_disbursement_per_loan",
            ),
        ),
    ]
