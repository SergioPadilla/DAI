"""
Created at 19/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template, request
from Practica2 import mandelbrot

app = Flask(__name__)


@app.route("/")
def init():
    return render_template('dynamic_image_index.html')


@app.route("/mandelbrot", methods=['GET'])
def process():
    x1 = float(request.args.get('x1'))
    y1 = float(request.args.get('y1'))
    x2 = float(request.args.get('x2'))
    y2 = float(request.args.get('y2'))
    pixels = int(request.args.get('pixels'))
    mandelbrot.renderizaMandelbrot(x1, y1, x2, y2, pixels, 100, 'static/fractal.png')
    return """
    <body>
        <img src='/static/fractal.png'>
    </body>
    """

if __name__ == "__main__":
    app.run()
