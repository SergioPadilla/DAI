"""
Created at 18/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <head>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    </head>
    <h1>Hello World!</h1>
    <img src="/static/logo.png">
    """

@app.route("/<path:path>")
def file(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run()