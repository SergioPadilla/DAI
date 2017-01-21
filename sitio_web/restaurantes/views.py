from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.
from .forms import AddForm
from .models import Restaurant
from django.conf import settings
import json


@login_required
def index(request):
    return render(request, 'home.html', {})


@login_required
def me(request):
    return render(request, 'me.html', {})


@login_required
def examples(request):
    return render(request, 'examples.html', {})


@login_required
def find(request):
    db = settings.MONGOCLIENT.test
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


@login_required
def add(request):
    if request.method == 'POST':
        form_post = AddForm(request.POST, request.FILES)
        message = ""

        if form_post.is_valid():
            db = settings.MONGOCLIENT.test
            id = form_post.cleaned_data.get('id')
            cuisine = form_post.cleaned_data.get('cuisine')
            name = form_post.cleaned_data.get('name')
            borough = form_post.cleaned_data.get('borough')
            result = db.restaurants.insert_one(
                {
                    'restaurant_id': id,
                    'cuisine': cuisine,
                    'name': name,
                    'borough': borough
                 })

            if result:
                print result.inserted_id
                message = 'El restaurante ha sido insertado con exito'
            else:
                message = 'Error insertando el restaurante'
        else:
            print(form_post.errors)

        template = 'mongo_example_add.html'
        context = {
            'message': message,
            'form': form_post
        }

        return render(request, template, context)

    return render(request, 'mongo_example_add.html', {'form': AddForm()})


@login_required
def findpage(request):
    db = settings.MONGOCLIENT.test
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


@login_required
def highcharts(request):
    return render(request, 'highcharts.html', {})


@login_required
def get_borough_data():
    db = settings.MONGOCLIENT.test
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

