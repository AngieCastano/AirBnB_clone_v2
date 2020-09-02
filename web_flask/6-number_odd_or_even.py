#!/usr/bin/python3
"""This displays “Hello HBNB!”"""
from flask import Flask, escape, render_template


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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
        """Show Python is cool[default]"""
        return 'Python %s' % escape(text).replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_integer(n):
        """displays only if n is an integer"""
        return '%s is a number' % escape(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_is_integer_template(n):
        """displays html template if n is an integer"""
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def n_is_integer_template_flow_control(n):
        """displays html template if n is an integer"""
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
        ''' when not imported'''
        app.run(host='0.0.0.0', port=5000)
