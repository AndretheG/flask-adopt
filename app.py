from flask import Flask, url_for, render_template, redirect, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm



app = Flask(__name__)

app.config['SECRET_KEY'] = 'asecretkey'

app.config['SQLACLCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLACLCHEMY_TRACK_MODIFICATIONS'] = False



connect_db(app)

with app.app_context():  ### use with app.app_context() when running Flask 3.0 or higher
    db.create_all()

toolbar = DebugToolbarExtension(app)

@app.route("/")
def pets_list():
    """List all pet names."""

    pets = Pet.query.all()
    return render_template("list.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def pets_add():
    """Add a new pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('list_pets'))
    
    else:
        return render_template("pet_add.html", form=form)
    

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit(pet_id):
    "Edit a pet."

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect(url_for('list_pets'))
    
    else:
        return render_template("edit.html", form=form, pet=pet)
    

@app.route("/api/pets/<int:pet_id>", methods=["GET"])
def get_pet_api(pet_id):
    """Return pet info in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)
