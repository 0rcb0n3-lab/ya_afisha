from environs import Env
import requests

from django.core.management.base import BaseCommand

from ._load_place_base import load_place

PLACES_DIRECTORY_URL = Env().str('PLACES_DIRECTORY_URL')


class Command(BaseCommand):
    help = 'Load all places from a GitHub directory of JSON files.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--directory',
            default=PLACES_DIRECTORY_URL,
            help='GitHub API URL of the directory with JSON files',
        )

    def handle(self, *args, **options):
        response = requests.get(options['directory'], timeout=30)
        response.raise_for_status()
        json_urls = [
            entry['download_url']
            for entry in response.json()
            if entry['type'] == 'file' and entry['name'].endswith('.json')
        ]
        for json_url in json_urls:
            place_data = requests.get(json_url, timeout=30).json()
            place = load_place(place_data)
            self.stdout.write(self.style.SUCCESS(f'  {place.title}'))