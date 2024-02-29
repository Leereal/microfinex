# myapp/management/commands/seeder.py

from django.core.management.base import BaseCommand
from apps.branch_assets.models import BranchAssets
from apps.branches.models import Branch
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

        self.stdout.write(self.style.SUCCESS('Fake data populated successfully for Branch, BranchAssets, and User'))
