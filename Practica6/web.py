"""
Created at 9/11/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
import json
import tweepy

from Practica6.rss_exercises.script_universal_feed_parser import get_news

twitter = {
    # Consumer keys and access tokens, used for OAuth
    'consumer_key': 'Gylisu2ec8wg9XGaE00Z1UVYu',
    'consumer_secret': 'xoDwaYA5irrNnsnzVVV55faJzBCw4qO5gNKrIy5i1AZ4UfIBZF',
    'access_token': '371991894-WIJiKeKfQuy8OR1mOIEs1gfMjQehobIS16HTdk9g',
    'access_token_secret': 'c6DywNLeAyVxv3yRFA9ACo25qcmTdCJhcwCsqVb8HyzaG'
}

app = Flask(__name__)
client = MongoClient()
db = client.test


@app.route("/", methods=['GET'])
def index():
    return render_template('home.html')


@app.route("/me", methods=['GET'])
def me():
    return render_template('me.html')


@app.route("/examples", methods=['GET'])
def examples():
    return render_template('examples.html')


@app.route("/mongo_examples", methods=['GET'])
def mongo_examples():
    return redirect('find')


@app.route("/find", methods=['GET', 'POST'])
def find():
    nperpage = 200
    if request.method == 'POST':
        key = str(request.form['key'])
        value = str(request.form['value']) if key != 'restaurant_id' else int(request.form['value'])
        cursor = db.restaurants.find({key: value})
        totalpages = 1
    else:
        total = db.restaurants.find().count()
        page = int(request.args.get("page")) if request.args.get("page") else 1
        totalpages = int(total / nperpage) + 1
        offset = (page-1)*nperpage
        cursor = db.restaurants.find().skip(offset).limit(nperpage)

    return render_template('mongo_example_find.html', cursor=cursor, totalpages=totalpages)


@app.route("/findpage")
def findpage():
    nperpage = 200
    page = int(request.args.get("page")) if request.args.get("page") else 1
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

    return json.dumps(restaurants)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        id = int(request.form['id'])
        cuisine = str(request.form['cuisine'])
        name = str(request.form['name'])
        borough = str(request.form['borough'])
        result = db.restaurants.insert_one(
            {
                'restaurant_id': id,
                'cuisine': cuisine,
                'name': name,
                'borough': borough
             })
        print result.inserted_id
        if result:
            message = 'El restaurante ha sido insertado con exito'
        else:
            message = 'Error insertando el restaurante'

        return render_template('mongo_example_add.html', message=message)
    return render_template('mongo_example_add.html')


@app.route("/remove", methods=['GET', 'POST'])
def remove():
    if request.method == 'POST':
        howmany = str(request.form['howmany'])
        key = str(request.form['key'])
        value = str(request.form['value']) if key != 'restaurant_id' else int(request.form['value'])

        if howmany == 'one':
            result = db.restaurants.delete_one({key: value})
        else:
            result = db.restaurants.delete_many({key: value})

        if result:
            message = 'Has borrado '+str(result.deleted_count)+' restaurantes'
        else:
            message = 'Error borrando el restaurante'

        return render_template('mongo_example_remove.html', message=message)
    return render_template('mongo_example_remove.html')


@app.route("/highcharts", methods=['GET'])
def highcharts():
    return render_template('highcharts.html')


@app.route("/get_borough_data", methods=['GET'])
def get_borough_data():
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

    return json.dumps(boroughs_array)


@app.route("/maps", methods=['GET'])
def maps():
    return render_template('maps.html')


@app.route("/twitter-timeline", methods=['GET'])
def twitter_timeline():
    return render_template('twitter-timeline.html')


@app.route("/tweets", methods=['GET'])
def tweets():
    texts = []
    value = str(request.args.get("search")) if str(request.args.get("search")) else "Granada"

    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(twitter['consumer_key'], twitter['consumer_secret'])
    auth.set_access_token(twitter['access_token'], twitter['access_token_secret'])
    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)
    # https://dev.twitter.com/docs/api/1.1/get/search/tweets
    tweet = api.search(q=value, count=10)

    for i in range(0, 9):
        texts.append(tweet[i].text)

    return render_template('slider.html', tweets=texts)


@app.route("/rss", methods=['GET'])
def rss():
    return render_template('rss.html', tweets=get_news())


@app.route("/mashup", methods=['GET'])
def mashup():
    return render_template('mashup.html')


@app.route("/get_mashup_data", methods=['GET'])
def get_mashup():
    result = []
    languages = ['es', 'en', 'fr', 'de', 'cs', 'ca', 'ga', 'it', 'ja', 'qu', 'ro', 'zh']
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(twitter['consumer_key'], twitter['consumer_secret'])
    auth.set_access_token(twitter['access_token'], twitter['access_token_secret'])
    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)

    for language in languages:
        data = []
        data.append(language)
        tweets = api.search(q="twitter", lang=language, count=100)
        data.append(len(tweets))
        result.append(data)

    return json.dumps(result)



if __name__ == "__main__":
    app.run()
