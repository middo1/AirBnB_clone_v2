#!/usr/bin/python3
"""Start a Flask app
"""
from flask import Flask

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


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
