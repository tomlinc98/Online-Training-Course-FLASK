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

@main.route('/blog', methods=['GET', 'POST'])
def blog(cat=None):
    return render_template('blog.html',  title='Blog')

@main.route('/basics', methods=['GET', 'POST'])
def basics(cat=None):
    return render_template('basics.html',  title='Basics of Scrum')

"""@app.route("/details/<int:pet_id>")
def pet_details(pet_id):
    # View function for Showing Details of Each Pet. # 
    pet = next((pet for pet in pets if pet["id"] == pet_id), None) 
    if pet is None: 
        abort(404, description="No Pet was Found with the given ID")
    return render_template("details.html", pet = pet) """