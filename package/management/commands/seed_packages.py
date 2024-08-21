from django.core.management.base import BaseCommand
from package.models import Package
import random
from datetime import datetime

class Command(BaseCommand):
    help = 'Seed the Package table with test data'

    def handle(self, *args, **kwargs):
        risks = ['B', 'M', 'A']

        packages = []
        for i in range(10):
            authorized = random.choice([True, False])
            authorized_at = datetime.now().date() if authorized else None

            package = Package(
                description=f'Package {i+1}',
                authorized=authorized,
                authorized_at=authorized_at,
                risk=random.choice(risks),
            )

            packages.append(package)

        Package.objects.bulk_create(packages)
        self.stdout.write(self.style.SUCCESS('Successfully seeded the Package table'))
