import requests

from django.core.management.base import BaseCommand

from ._load_place_base import load_place_from_dict


class Command(BaseCommand):
    help = 'Load places from JSON files provided as URLs.'

    def add_arguments(self, parser):
        parser.add_argument('json_urls', nargs='+', help='URLs of JSON place files')

    def handle(self, *args, **options):
        for json_url in options['json_urls']:
            data = requests.get(json_url, timeout=30).json()
            place = load_place_from_dict(data)
            self.stdout.write(self.style.SUCCESS(f'  {place.title}'))