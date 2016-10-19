"""
Created at 18/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, send_from_directory, render_template
app = Flask(__name__)

@app.route("/user/<user>")
def init(user):
    return send_from_directory('static/users/', user+'.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
