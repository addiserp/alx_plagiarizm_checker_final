#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template
from os import environ
import uuid
from models import storage
from models.biddoc import Biddoc


app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/', strict_slashes=False)
def index():
    """ Alx Plagiarizm Checker is alive! """
    
    return render_template('main-layout.html',cache_id=str(uuid.uuid4()))

@app.route('/contacts', strict_slashes=False)
def contact():
    """ Alx Plagiarizm Checker  contacts page! """
    
    return render_template('pages-contact.html',cache_id=str(uuid.uuid4()))

@app.route('/login', strict_slashes=False)
def login():
    """ Alx Plagiarizm Checker  loginpage page! """
    
    return render_template('pages-login.html',cache_id=str(uuid.uuid4()))

@app.route('/register', strict_slashes=False)
def register():
    """ Alx Plagiarizm Checker  loginpage page! """
    
    return render_template('pages-register.html',cache_id=str(uuid.uuid4()))

@app.route('/profile', strict_slashes=False)
def profile():
    """ Alx Plagiarizm Checker  profile page! """
    
    return render_template('users-profile.html',cache_id=str(uuid.uuid4()))

@app.route('/dashboard', strict_slashes=False)
def dashboard():
    """ Alx Plagiarizm Checker  dashboard page! """
    
    return render_template('pages-dashboard.html',cache_id=str(uuid.uuid4()))

@app.route('/about', strict_slashes=False)
def about():
    """ Alx Plagiarizm Checker  about page! """

    return render_template('pages-landing.html', cache_id=str(uuid.uuid4()))


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5001)
