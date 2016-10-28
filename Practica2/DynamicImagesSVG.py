"""
Created at 27/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask
import svgwrite
from random import randint

app = Flask(__name__)


@app.route("/")
def init():
    width = str(randint(100, 200))
    height = str(randint(50, 100))
    r = str(randint(0, 255))
    g = str(randint(0, 255))
    b = str(randint(0, 255))
    svg_document = svgwrite.Drawing(filename="static/test-svgwrite.svg", size=("800px", "600px"))
    m = randint(0, 3)
    if m == 1:
        color = 'green'
    elif m == 2:
        color = 'black'
    else:
        color = 'pink'
    n = randint(0, 3)
    if n == 1:
        svg_document.add(svg_document.rect(insert=(randint(100, 500), randint(100, 500)),
                                           size=(width + "px", height + "px"),
                                           stroke_width="1",
                                           stroke=color,
                                           fill="rgb(" + r + "," + g + "," + b + ")"))
    elif n == 2:
        svg_document.add(svg_document.ellipse(center=(randint(500, 1000), randint(500, 1000)),
                                              r=(randint(100, 500), randint(100, 500)),
                                              stroke_width="1",
                                              stroke=color,
                                              fill="rgb(" + r + "," + g + "," + b + ")"))
    else:
        svg_document.add(svg_document.circle(center=(randint(500, 1000), randint(500, 1000)),
                                             r=randint(100, 500),
                                             stroke_width="1",
                                             stroke=color,
                                             fill="rgb(" + r + "," + g + "," + b + ")"))
    print(svg_document.tostring())
    svg_document.save()
    return """
    <body>
        <img src='static/test-svgwrite.svg'></img>
    </body>
    """


if __name__ == "__main__":
    app.run()
