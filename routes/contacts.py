from flask import Blueprint, render_template, request, redirect
from utils.db import db
from models.contact import Contact

contacts = Blueprint('contact', __name__)

@contacts.route('/')
def home():
    return render_template('index.html')

@contacts.route('/new', methods=['POST'])
def add_contact():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    new_contact = Contact(fullname, email, phone)

    db.session.add(new_contact)
    db.session.commit()

    return redirect('/')

@contacts.route('/update')
def update():
    return "jh"

@contacts.route('/delete')
def delete():
    return "jh"

@contacts.route('/about')
def about():
    return render_template('about.html')