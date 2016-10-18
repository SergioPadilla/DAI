"""
Created at 18/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, url_for
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

if __name__ == "__main__":
    app.run()