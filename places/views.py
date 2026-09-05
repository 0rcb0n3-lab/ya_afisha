from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


# Create your views here.
def index(request):
    places = Place.objects.all()

    features = []

    for place in places:
        features.append(
            {
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
        )

    geojson = {
        "type": "FeatureCollection",
        "features": features,
    }

    return render(request, "index.html", {"places_geojson": geojson})


def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    images = place.images.all()

    data = {
        "title": place.title,
        "imgs": [image.image.url for image in images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": str(place.lat),
            "lng": str(place.lng),
        },
    }

    return JsonResponse(data, json_dumps_params={"ensure_ascii": False, "indent": 2})
