from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:superpaloman+12@localhost/contactsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.register_blueprint(contacts)
