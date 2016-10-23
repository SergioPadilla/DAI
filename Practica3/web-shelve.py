"""
Created at 23/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template, request, redirect, url_for, session
import os
import shelve

from Practica3.Forms.Register import RegistrationForm
from Practica3.Utils.User import User

app = Flask(__name__)

# Open shelve
db = shelve.open('test-shelve.db')

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
TEMPLATES_DIR = os.path.join(SITE_ROOT, '/templates/')


@app.route("/", methods=['GET', 'POST'])
def index():


if __name__ == "__main__":
    app.run()