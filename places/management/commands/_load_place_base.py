import requests

from django.core.files.base import ContentFile

from places.models import Place, PlaceImage


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
        image = PlaceImage(place=place, ordering=ordering)
        image.image.save(basename(img_url), ContentFile(image_data), save=True)
    return place


def download_image(url):
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.content


def basename(url):
    return url.rsplit('/', 1)[-1]