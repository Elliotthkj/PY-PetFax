# petfax/pet.py
from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")
bp_facts = Blueprint('facts', __name__, url_prefix="/facts")


@bp.route('/')
def index():
    return render_template('index.html', pets=pets)


@bp.route('/<int:pet_id>')
def show(pet_id):
    pet = pets[pet_id - 1]
    return render_template('show.html', pet=pet)


@bp_facts.route('/new', methods=['GET'])
def create_fact():
    return render_template('create.html')
