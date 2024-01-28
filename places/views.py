from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place


def main_page(request):
    context = {
        'data': {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [37.62, 55.793676]
                    },
                    "properties": {
                        "title": "«Легенды Москвы",
                        "placeId": "moscow_legends",
                        "detailsUrl": 'static/places/moscow_legends.json'

                    }
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [37.64, 55.753676]
                    },
                    "properties": {
                        "title": "Крыши24.рф",
                        "placeId": "roofs24",
                        "detailsUrl": "static/places/roofs24.json"
                    }
                }
            ]
        }
    }
    return render(request, 'index.html', context=context)
