from flask import render_template, Blueprint
from iamdev import app

home_blueprint = Blueprint('home', __name__)
@home_blueprint.get('/')
def home():
    return render_template('webpages/home.html')


