from flask import Blueprint, render_template

contacts = Blueprint('contact', __name__)

@contacts.route('/')
def home():
    return render_template('index.html')

@contacts.route('/new')
def add_contact():
    return "jh"

@contacts.route('/update')
def update():
    return "jh"

@contacts.route('/delete')
def delete():
    return "jh"

@contacts.route('/about')
def about():
    return render_template('about.html')