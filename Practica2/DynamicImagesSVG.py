"""
Created at 27/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template
import svgwrite
from random import randint

app = Flask(__name__)


@app.route("/")
def init():
    number = randint(1, 100)
    svg_document = svgwrite.Drawing(filename="test-svgwrite.svg", size=("800px", "600px"))
    svg_document.add(svg_document.rect(insert=(0, 0),
                                       size=("200px", "100px"),
                                       stroke_width="1",
                                       stroke="black",
                                       fill="rgb(255,255,0)"))
    print(svg_document.tostring())
    svg_document.save()
    return """
    <body>
        <img src='static/test-svgwrite.svg'></img>
    </body>
    """


if __name__ == "__main__":
    app.run()
