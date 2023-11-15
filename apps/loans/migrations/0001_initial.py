# Generated by Django 4.2.4 on 2023-11-09 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0001_initial'),
        ('currencies', '0001_initial'),
        ('loan_products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ref_code', models.CharField(editable=False, max_length=20, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('loan_term', models.PositiveIntegerField()),
                ('application_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('approval_date', models.DateField(blank=True, null=True)),
                ('disbursement_date', models.DateField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='clients.client')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_loans', to=settings.AUTH_USER_MODEL)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='currencies.currency')),
                ('loan_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loan_products.loanproduct')),
            ],
            options={
                'verbose_name': 'Loan',
                'verbose_name_plural': 'Loans',
            },
        ),
    ]
