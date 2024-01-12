#!/usr/bin/python3
""" start a flask web application"""

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ return text"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def bhnb():
    """ return text"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ return text"""
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    return 'Python {}'.format(escape(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
