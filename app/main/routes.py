from flask import Blueprint, render_template, redirect, url_for, request
from app.models import User

main = Blueprint('main', __name__)

@main.route('/')

@main.route('/index', methods=['GET', 'POST'])
def index(cat=None):
    return render_template('index.html',  title='Home')

@main.route('/courses', methods=['GET', 'POST'])
def courses(cat=None):
    return render_template('courses.html',  title='Courses')

@main.route('/about', methods=['GET', 'POST'])
def about(cat=None):
    return render_template('about.html',  title='About')

