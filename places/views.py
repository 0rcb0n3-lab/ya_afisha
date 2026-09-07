from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from places.models import Place


# Create your views here.
def index(request):
    return render(
        request,
        "index.html",
        {
            "places_geojson": {
                "type": "FeatureCollection",
                "features": [place.as_feature() for place in Place.objects.all()],
            }
        },
    )


def place_detail(request, pk):
    place = get_object_or_404(Place.objects.prefetch_related('images'), pk=pk)
    return JsonResponse(
        place.as_json(),
        json_dumps_params={"ensure_ascii": False, "indent": 2},
    )
