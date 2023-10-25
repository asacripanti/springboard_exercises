"""Pet Adoption app"""

from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from models import Pet, db, connect_db
from forms import addPetForm, editPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


connect_db(app)
# db.create_all()

with app.app_context():
    db.create_all()

@app.route('/')
def home_page():
    """Home page that lists pets"""

    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Form to add pets for adoption"""
    form = addPetForm()    
    if form.validate_on_submit():
        name = request.form['name']
        species = request.form['species']
        photo_url = request.form['photo_url']
        age = request.form['age']
        notes = request.form['notes']

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template ("add_pet_form.html", form=form)


@app.route('/<int:pet_id>')
def pet_info(pet_id):
    """Specific pet info"""

    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_info.html', pet=pet)


@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet_info(pet_id):
    """Edit pet info"""

    pet = Pet.query.get_or_404(pet_id)
    form = editPetForm()

    if form.validate_on_submit():

        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect('/')

    else:
        return render_template ("pet_edit.html", pet=pet, form=form)






