#!/usr/bin/python3
"""Start a Flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_flask():
    """Return string when route queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """Return string when route queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def hello_c(text):
    """Return string when route queried
    """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def hello_python(text='is cool'):
    """Return string when route queried
    """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>')
def hello_num(n=None):
    """Return string when route queried
    """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """Retrieve template for request
    """
    path = '5-number.html'
    return render_template(path, n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Render template based on conditional
    """
    path = '6-number_odd_or_even.html'
    return render_template(path, n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
