"""
Created at 9/11/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('home.html')


@app.route("/me", methods=['GET'])
def me():
    return render_template('me.html')


@app.route("/tutoriales", methods=['GET'])
def tutorials():
    return render_template('tutorials.html')


if __name__ == "__main__":
    app.run()
