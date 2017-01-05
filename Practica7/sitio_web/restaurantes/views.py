from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.
from .models import Restaurant
from pymongo import MongoClient
import json


def index(request):
    return render(request, 'home.html', {})


def me(request):
    return render(request, 'me.html', {})


def examples(request):
    return render(request, 'examples.html', {})


def find(request):
    client = MongoClient()
    db = client.test
    nperpage = 200
    total = db.restaurants.find().count()
    page = int(request.GET.get('page', 1))
    totalpages = range(1, int(total / nperpage) + 2)  # 2 because start in 1
    offset = (page - 1) * nperpage
    cursor = db.restaurants.find().skip(offset).limit(nperpage)

    template = 'mongo_example_find.html'
    context = {
        'cursor': cursor,
        'totalpages': totalpages
    }

    return render(request, template, context)


def findpage(request):
    client = MongoClient()
    db = client.test
    nperpage = 200
    page = int(request.GET.get('page', 1))
    offset = (page - 1) * nperpage
    cursor = db.restaurants.find().skip(offset).limit(nperpage)
    restaurants = []

    for document in cursor:
        restaurant = {
            'restaurant_id': document["restaurant_id"],
            'cuisine': document["cuisine"],
            'borough': document["borough"],
            'name': document["name"]
        }
        restaurants.append(restaurant)

    return HttpResponse(json.dumps(restaurants))


def highcharts(request):
    return render(request, 'highcharts.html', {})


def get_borough_data(request):
    client = MongoClient()
    db = client.test
    boroughs = {}
    cursor = db.restaurants.find()
    for document in cursor:
        borough = document['borough']
        if borough in boroughs:
            count = boroughs[borough]
            count += 1
            boroughs[borough] = count
        else:
            boroughs[borough] = 0

    boroughs_array = []
    for borough in boroughs:
        json_object = {
            'name': borough,
            'y': boroughs[borough]
        }
        boroughs_array.append(json_object)

    return HttpResponse(json.dumps(boroughs_array))

