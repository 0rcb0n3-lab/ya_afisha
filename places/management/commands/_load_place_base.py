import sys

import requests

from django.core.files.base import ContentFile

from places.models import Place, PlaceImage


def get_error_message(decoded_response):
    if not isinstance(decoded_response, dict):
        return None
    for key in ('error', 'message'):
        if key in decoded_response:
            return decoded_response[key]
    return None


def load_place(data):
    place, _ = Place.objects.update_or_create(
        title=data['title'],
        defaults={
            'description_short': data['description_short'],
            'description_long': data['description_long'],
            'lng': float(data['coordinates']['lng']),
            'lat': float(data['coordinates']['lat']),
        },
    )

    place.images.all().delete()
    for ordering, img_url in enumerate(data['imgs']):
        image_data = download_image(img_url)
        PlaceImage.objects.create(
            place=place,
            ordering=ordering,
            image=ContentFile(image_data, name=basename(img_url)),
        )
    return place


def download_image(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.RequestException as error:
        sys.exit(f'Не удалось загрузить изображение {url}: {error}')
    return response.content


def basename(url):
    return url.rsplit('/', 1)[-1]
