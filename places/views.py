from django.shortcuts import render
from places.models import Place


# Create your views here.
def index(request):
    places = Place.objects.all()

    features = []

    details_urls = {
        "Экскурсионный проект «Крыши24.рф»": "static/places/roofs24.json",
        "Экскурсионная компания «Легенды Москвы»": "static/places/moscow_legends.json",
    }

    
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
                    "detailsUrl": details_urls[place.title],
                },
            }
        )

    geojson = {
        "type": "FeatureCollection",
        "features": features,
    }

    return render(request, "index.html", {"places_geojson": geojson})
