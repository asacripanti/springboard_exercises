"""Pet Adoption app"""

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Pet, db, connect_db

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """Home page that lists pets"""

    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)
