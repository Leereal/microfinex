# myapp/management/commands/seeder.py

from decimal import Decimal
from django.core.management.base import BaseCommand
from apps.branch_assets.models import BranchAssets
from apps.branch_product.models import BranchProduct
from apps.branches.models import Branch
from apps.currencies.models import Currency
from apps.periods.models import Period
from apps.products.models import Product
from apps.users.models import User, UserBranch
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populate Branch, BranchAssets, and User models with fake data'

    def handle(self, *args, **options):
        fake = Faker()

        # Generate Branches
        for _ in range(20):
            branch = Branch.objects.create(
                name=fake.city(),
                address=fake.address(),
                email=fake.email(),
                phone=fake.phone_number(),
                is_active=True,
                country=fake.country()
            )

        office_items = ['laptop', 'car', 'TV', 'chair', 'desk', 'printer', 'phone', 'monitor', 'keyboard', 'mouse']

        # Generate BranchAssets
        for branch in Branch.objects.all():
            item = random.choice(office_items)
            branch_asset = BranchAssets.objects.create(
                branch=branch,
                item=item,
                description=fake.text(),
                brand=fake.company(),
                color=fake.color_name(),
                quantity=fake.random_int(min=1, max=100),
                user_id=1,
                used_by_id=1,
                purchase_date=fake.date_between(start_date="-1y", end_date="today"),
                images=[]  # You may adjust this field based on your requirements
            )

        # Generate Users
        for _ in range(20):
            email = fake.unique.email()  # Ensure unique email addresses
            user = User.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=email,
                is_staff=fake.boolean(chance_of_getting_true=20),  # Example of a boolean field
                is_active=True,
                date_joined=fake.date_time_between(start_date="-1y", end_date="now"),
            )

            # Assign random branches to users
            branches = Branch.objects.order_by('?')[:random.randint(1, 3)]
            for branch in branches:
                UserBranch.objects.create(user=user, branch=branch, created_by_id=1)
        
        # Generate Periods
        # Customized names and their corresponding duration units
        period_details = [
            {"name": "Weekly", "units": ["weeks"]},
            {"name": "Monthly", "units": ["months"]},
            {"name": "Daily", "units": ["days"]},
            {"name": "Yearly", "units": ["years"]},
            {"name": "Quarterly", "units": ["months"]}
        ]

        for period_detail in period_details:
            # Select a name and its valid units
            name = period_detail["name"]
            valid_units = period_detail["units"]
            
            # Ensure the duration matches the unit for names with specific time frames
            if name == "Quarterly":
                # Assuming quarterly means 3 months duration
                duration = 3
                duration_unit = "months"
            elif name == "Yearly":
                duration = 1
                duration_unit = "years"
            else:
                # For other types, you can randomize within a sensible range if needed
                duration = fake.random_int(min=1, max=4)
                duration_unit = random.choice(valid_units)

            Period.objects.create(
                name=name,
                duration=str(duration),
                duration_unit=duration_unit,
                description=fake.text()
            )

        # Generate Products
        # Predefined product names
        product_names = ["SSB", "Paynet", "Loan Term", "Collateral Based"]

        # Generate Products with predefined names
        for name in product_names:
            Product.objects.create(
                name=name,
                is_active=fake.boolean(chance_of_getting_true=75)  # 75% chance to be active
            )
        

        # Generate Specific Currencies
        currencies = [
            {"name": "US Dollar", "code": "USD", "symbol": "$", "position": "before"},
            {"name": "Zim Dollar", "code": "ZWL", "symbol": "Z$", "position": "before"},
            {"name": "SA Rand", "code": "ZAR", "symbol": "R", "position": "before"},
            {"name": "Botswana Pula", "code": "BWP", "symbol": "P", "position": "before"},
        ]

        for currency in currencies:
            Currency.objects.create(
                name=currency["name"],
                code=currency["code"],
                symbol=currency["symbol"],
                position=currency["position"],
                is_active=True
            )
        
        # Generate BranchProducts
        branches = list(Branch.objects.all())
        products = list(Product.objects.all())
        periods = list(Period.objects.all())
        users = list(User.objects.all())

        for _ in range(10):  # Adjust the number of BranchProducts to generate as needed
            branch_product = BranchProduct.objects.create(
                branch=random.choice(branches),
                product=random.choice(products),
                interest=Decimal(fake.random_number(digits=2) + fake.random_number(digits=2) / 100),
                max_amount=Decimal(fake.random_number(digits=5)),
                min_amount=Decimal(fake.random_number(digits=3)),
                period=random.choice(periods),
                min_period=fake.random_int(min=1, max=12),
                max_period=fake.random_int(min=13, max=24),            
                created_by=random.choice(users)
            )



        self.stdout.write(self.style.SUCCESS('Fake data populated successfully for Branch, BranchAssets, and User'))
