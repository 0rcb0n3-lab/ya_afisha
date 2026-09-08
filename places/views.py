from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def place_to_feature(place):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat],
        },
        "properties": {
            "title": place.title,
            "placeId": place.pk,
            "detailsUrl": reverse("place_detail", kwargs={"pk": place.pk}),
        },
    }


def place_to_json(place):
    return {
        "title": place.title,
        "imgs": [img.image.url for img in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng,
        },
    }


def index(request):
    return render(
        request,
        "index.html",
        {
            "places_geojson": {
                "type": "FeatureCollection",
                "features": [place_to_feature(place) for place in Place.objects.all()],
            }
        },
    )


def place_detail(request, pk):
    place = get_object_or_404(Place.objects.prefetch_related('images'), pk=pk)
    return JsonResponse(
        place_to_json(place),
        json_dumps_params={"ensure_ascii": False, "indent": 2},
    )
