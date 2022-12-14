from flask import Blueprint, render_template, redirect, url_for, request
from app.models import User, Announcement

main = Blueprint('main', __name__)

@main.route('/')

@main.route('/home', methods=['GET', 'POST'])
def home(cat=None):
    announcements = Announcement.query.order_by(Announcement.created_at).all()
    return render_template('home.html',  title='Home', announcements=announcements)

@main.route('/contact', methods=['GET', 'POST'])
def contact(cat=None):
    return render_template('contact.html',  title='Contact')  

@main.route('/courses', methods=['GET', 'POST'])
def courses(cat=None):
    return render_template('courses.html',  title='Courses')

@main.route('/about', methods=['GET', 'POST'])
def about(cat=None):
    return render_template('about.html',  title='About')

@main.route('/blog', methods=['GET', 'POST'])
def blog(cat=None):
    return render_template('blog.html',  title='Blog')

@main.route('/blog-form', methods=['GET', 'POST'])
def blogform(cat=None):
    return render_template('blog-form.html',  title='Blog Form')

@main.route('/terms', methods=['GET', 'POST'])
def terms(cat=None):
    return render_template('legal/terms.html',  title='Terms & Conditions')

@main.route('/policy', methods=['GET', 'POST'])
def policy(cat=None):
    return render_template('legal/policy.html',  title='Privacy Policy')

@main.route('/admin', methods=['GET', 'POST'])
def admin(cat=None):
    return render_template('admin/admin.html',  title='Admin')

"""@app.route("/details/<int:pet_id>")
def pet_details(pet_id):
    # View function for Showing Details of Each Pet. # 
    pet = next((pet for pet in pets if pet["id"] == pet_id), None) 
    if pet is None: 
        abort(404, description="No Pet was Found with the given ID")
    return render_template("details.html", pet = pet) """