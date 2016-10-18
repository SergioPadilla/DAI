"""
Created at 19/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template
import mandelbrot

app = Flask(__name__)

@app.route("/" )
def init():
    return render_template('dynamic_image_index.html')

@app.route("/mandelbrot/<x1>/<y1>/<x2>/<y2>/<pixels>", methods=['GET'])
def process(x1,y1,x2,y2,pixels):
    mandelbrot.renderizaMandelbrot(x1, y1, x2, y2, pixels, 100, 'fractal.png')
    return "<img src='fractal.png'>"

if __name__ == "__main__":
    app.run()