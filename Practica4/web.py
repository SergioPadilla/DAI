"""
Created at 9/11/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
db = client.test

# for document in cursor:
#     print(document)


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

if __name__ == "__main__":
    app.run()
