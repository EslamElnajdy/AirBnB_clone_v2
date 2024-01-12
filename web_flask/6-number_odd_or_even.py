#!/usr/bin/python3
""" start a flask web application"""

from flask import Flask, escape, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_template_route(n):
    if n % 2 == 0:
        num_type = 'even'
    else:
        num_type = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, T=num_type)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
