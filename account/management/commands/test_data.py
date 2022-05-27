import random
import string

from django.core.management.base import BaseCommand

from account.models import Individual, Entity, Department


class Command(BaseCommand):
    help = 'Filling with test data'

    def handle(self, *args, **options):
        individual = [Individual(id=str(i) + '01') for i in range(1, 13)]
        for i in individual:
            i.full_name = ''.join([random.choice(string.ascii_lowercase) for i in range(16)])
        # Individual.objects.all().delete()
        Individual.objects.bulk_create(individual)
        entity = [Entity(id=str(i) + '02') for i in range(1, 14)]
        for i in entity:
            i.full_title = ''.join([random.choice(string.ascii_lowercase) for i in range(16)])
        # Entity.objects.all().delete()
        Entity.objects.bulk_create(entity)
        department = [Department(id=str(i) + '03') for i in range(1, 12)]
        for i in department:
            i.title = ''.join([random.choice(string.ascii_lowercase) for i in range(16)])
        Department.objects.all().delete()
        Department.objects.bulk_create(department)
        self.stdout.write(self.style.SUCCESS('Successfully created'))
