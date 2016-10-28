"""
Created at 19/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template, request
from Practica2 import mandelbrot
import os
import time

app = Flask(__name__)


@app.route("/")
def init():
    return render_template('dynamic_image_index.html')


@app.route("/mandelbrot", methods=['GET'])
def process():
    remove_old_files()
    x1 = float(request.args.get('x1'))
    y1 = float(request.args.get('y1'))
    x2 = float(request.args.get('x2'))
    y2 = float(request.args.get('y2'))
    pixels = int(request.args.get('pixels'))
    paleta = request.args.get('paleta')
    if paleta:
        paleta = int(request.args.get('paleta'))
        colors = [(235, 120, 43), (101, 230, 210), (15, 45, 102)] if paleta == 1 else [(255, 0, 255), (54, 255, 36),
                                                                                       (234, 6, 24)]
        n = int(request.args.get('n'))
        name = '%f%f%f%f%d%d%d' % (x1, y1, x2, y2, pixels, paleta, n)
        if not os.path.exists('static/'+name+'.png'):
            mandelbrot.renderizaMandelbrotBonito(x1, y1, x2, y2, pixels, 100, 'static/mandelbrot/'+name+'.png', colors, n)
    else:
        name = '%f%f%f%f%d' % (x1, y1, x2, y2, pixels)
        if not os.path.exists('static/' + name + '.png'):
            mandelbrot.renderizaMandelbrot(x1, y1, x2, y2, pixels, 100, 'static/mandelbrot/'+name+'.png')
    return """
    <body>
        <img src='static/mandelbrot/%s.png'>
    </body>
    """ % name


def remove_old_files():
    path = '/Users/sergiopadilla/github/DAI/Practica2/static/mandelbrot'
    now = time.time()
    seconds_day = 24*60*60
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.stat(f).st_mtime < now - seconds_day:
            os.remove(os.path.join(path, f))


if __name__ == "__main__":
    app.run()
