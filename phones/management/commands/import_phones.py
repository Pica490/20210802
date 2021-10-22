import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('insert')

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:

            name = phone['name']
            image = phone['image']
            price = phone['price']
            release_date = phone['release_date']
            lte_exist = phone['lte_exists']

            p = Phone.objects.create(name=name, price=price, image = image, release_date = release_date, lte_exist = lte_exist, slug = name)
            p.save()


