#!/usr/bin/python3
"""This displays “Hello HBNB!”"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_session():
        """close sqlalchemy session"""
        storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list(n):
        """state list"""
        return render_template('7-states_list.html', states=storage.all(State))


if __name__ == '__main__':
        ''' when not imported'''
        app.run(host='0.0.0.0', port=5000)
