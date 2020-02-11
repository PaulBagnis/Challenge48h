import os
from werkzeug import secure_filename
from flask import Flask, request, redirect, url_for, render_template, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


app = Flask(__name__)
app.config.from_object("project.config.Config")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


from .forms import PatientForm, MedicForm

from .models import *
@app.route("/", methods=["GET", "POST"])

@app.route("/index", methods=["GET", "POST"])
def index():
    form = PatientForm()

    if request.method == "POST":
        if form.validate() == False:
            flash("All fields are required.")
            return render_template("index.html", title="Gloth", subtitle="test", patient_form=form, name="Ynov")
        else:
            data = request.args.get(form)
            return redirect(url_for('medicaments'), data=data)

    return render_template("index.html", title="Gloth", subtitle="subtitle", patient_form=form, name="Ynov")

@app.route('/ordonnance', methods=["GET"])
def posology():
    # query = db.session.query(ClassesFamilies,Molecules,Medication).filter(ClassesFamilies==).filter(Molecules.id==ClassesFamilies.molecule_id).filter(Molecules.id==Medication.molecule_id).all()
    return render_template("ordonnance.html", query=query, name="Ynov")

@app.route('/medicaments', methods=["GET","POST"])
def medicaments():

    return render_template("medicaments.html", name="Ynov")