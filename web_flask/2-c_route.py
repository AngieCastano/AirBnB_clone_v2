#!/usr/bin/python3
"""This displays “Hello HBNB!”"""
from flask import Flask, escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
        """Print hello hbnb"""
        return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
        """Print hbnb"""
        return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
            """Show c and text"""
            return 'C %s' % escape(text).replace("_", " ")


if __name__ == '__main__':
        ''' when not imported'''
        app.run(host='0.0.0.0', port=5000)
