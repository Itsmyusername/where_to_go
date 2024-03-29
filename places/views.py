from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place


def main_page(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse(place_details, args=[place.id])

            }
        })
    context = {
        "data": {
            "type": "FeatureCollection",
            "features": features
        }
    }
    return render(request, "index.html", context=context)


def place_details(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related("images"), id=place_id)
    data = {
        "title": place.title,
        "imgs": [image.img.url for image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lon
        }
    }
    return JsonResponse(data, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 2})
