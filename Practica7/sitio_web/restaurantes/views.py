from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.
from .models import Restaurant


def index(request):
    return render(request, 'home.html', {})


def me(request):
    return render(request, 'me.html', {})


def examples(request):
    return render(request, 'examples.html', {})


def find(request):
    nperpage = 200
    restaurant_list = Restaurant.objects.all()
    # total = Restaurant.objects.count()
    # totalpages = int(total / nperpage) + 1
    template = 'mongo_example_find.html'
    context = {
        'cursor': restaurant_list
    }

    return render(request, template, context)
    # nperpage = 200
    # if request.method == 'POST':
    #     key = str(request.form['key'])
    #     value = str(request.form['value']) if key != 'restaurant_id' else int(request.form['value'])
    #     cursor = db.restaurants.find({key: value})
    #     totalpages = 1
    # else:
    #     total = db.restaurants.find().count()
    #     page = int(request.args.get("page")) if request.args.get("page") else 1
    #     totalpages = int(total / nperpage) + 1
    #     offset = (page-1)*nperpage
    #     cursor = db.restaurants.find().skip(offset).limit(nperpage)
    #
    # return render(request, 'mongo_example_find.html', {cursor=cursor, totalpages=totalpages})


def highcharts(request):
    return render(request, 'highcharts.html', {})
