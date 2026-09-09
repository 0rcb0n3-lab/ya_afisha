import sys

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from ._load_place_base import get_error_message, load_place


class Command(BaseCommand):
    help = 'Load all places from a GitHub directory of JSON files.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--directory',
            default=settings.PLACES_DIRECTORY_URL,
            help='GitHub API URL of the directory with JSON files',
        )

    def handle(self, *args, **options):
        try:
            response = requests.get(options['directory'], timeout=30)
            response.raise_for_status()
            decoded_response = response.json()
            error_message = get_error_message(decoded_response)
            if error_message:
                raise requests.HTTPError(f'ошибка в теле ответа: {error_message}')
        except requests.RequestException as error:
            sys.exit(
                f'Не удалось получить список файлов: {error}\n'
                'Проверьте переменную PLACES_DIRECTORY_URL в .env'
            )
        json_urls = [
            entry['download_url']
            for entry in decoded_response
            if entry['type'] == 'file' and entry['name'].endswith('.json')
        ]
        for json_url in json_urls:
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