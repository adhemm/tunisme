from flask import Blueprint
from flask import url_for, jsonify, render_template

home = Blueprint('home', __name__)


@home.route('/')
@home.route('/index')
@home.route('/home')
def index():
    # "index.html" in "app" templates folder
    return(render_template('index.html'))