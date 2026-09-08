import sys

import requests

from django.core.management.base import BaseCommand

from ._load_place_base import get_error_message, load_place


class Command(BaseCommand):
    help = 'Load places from JSON files provided as URLs.'

    def add_arguments(self, parser):
        parser.add_argument('json_urls', nargs='+', help='URLs of JSON place files')

    def handle(self, *args, **options):
        for json_url in options['json_urls']:
            try:
                response = requests.get(json_url, timeout=30)
                response.raise_for_status()
                decoded_response = response.json()
                error_message = get_error_message(decoded_response)
                if error_message:
                    raise requests.HTTPError(f'ошибка в теле ответа: {error_message}')
            except requests.RequestException as error:
                sys.exit(f'Не удалось загрузить данные по адресу {json_url}: {error}')
            place = load_place(decoded_response)
            self.stdout.write(self.style.SUCCESS(f'  {place.title}'))