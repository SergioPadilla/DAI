"""
Created at 19/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()