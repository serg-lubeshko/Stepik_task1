import random

from django.http import Http404
from django.shortcuts import render

from .data.data import tours, departures, description, subtitle, title


def main_view(request):
    random_tours = random.sample(list(tours.items()), k=6, )

    context = {
        'title': title,
        'departures': departures,
        'subtitle': subtitle,
        'description': description,
        'tours': dict(random_tours),

    }
    return render(request, template_name='tours/index.html', context=context)


def departure_view(request, departure):
    if departure not in departures.keys():
        raise Http404
    tours_departure = {key: val for key, val in tours.items() if val['departure'] == departure}
    max_price = (max(tours_departure.values(), key=lambda x: x['price']))['price']
    min_price = (min(tours_departure.values(), key=lambda x: x['price']))['price']
    max_nights = (max(tours_departure.values(), key=lambda x: x['nights']))['nights']
    min_nights = (min(tours_departure.values(), key=lambda x: x['nights']))['nights']
    count_tours = len(tours_departure)
    context = {
        'title': title,
        'departures': departures,
        'tours': tours_departure,
        'output': departures[departure],
        'count': count_tours,
        'max_price': max_price,
        'min_price': min_price,
        'max_nights': max_nights,
        'min_nights': min_nights
    }
    return render(request, template_name='tours/departure.html', context=context)


def tour_view(request, pk):
    if pk not in tours.keys():
        raise Http404
    tour = tours.get(pk)
    context = {
        'title': title,
        'departures': departures,
        'tour': tour,
        'stars': int(tour['stars']) * "★",
        'departure': departures[tour["departure"]],
        'nights': tour['nights'],
        'country': tour['country'],
        'picture': tour['picture'],
        'description': tour['description'],
        'price': tour['price'],
        'titles': tour['title']
    }

    return render(request, template_name='tours/tour.html', context=context)
