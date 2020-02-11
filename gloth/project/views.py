import os
from werkzeug import secure_filename
from flask import Flask, request, redirect, url_for, render_template, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import sqlalchemy

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

<<<<<<< HEAD
@app.route('/ordonnance', methods=["GET"])
def posology():
    # query = db.session.query(ClassesFamilies,Molecules,Medication).filter(ClassesFamilies==).filter(Molecules.id==ClassesFamilies.molecule_id).filter(Molecules.id==Medication.molecule_id).all()
    return render_template("ordonnance.html", query=query, name="Ynov")
=======
@app.route('/select', methods=["GET", "POST"])
def select():

    result = db.engine.execute("select distinct medication.name from molecules, medication where molecules.id = medication.molecule_id and molecules.id = " + str(1))
    molMed = [row[0] for row in result]

    result = db.engine.execute("select molecules.name from molecules, pathology, treatment_molecule where molecules.id = treatment_molecule.molecule_id and treatment_molecule.pathology_id = pathology.id and treatment_molecule.pathology_name =" + "'LA GOUTTE'")
    patMol = [row[0] for row in result]
    
    result = db.engine.execute("select molecules.name from classes_families, classes, molecules where classes_families.class_id = classes.id and classes_families.molecule_id = molecules.id and classes.id = " + str(1))
    molCla = [row[0] for row in result]
    
    result = db.engine.execute("select distinct pathology_name from molecules, pathology, treatment_molecule where molecules.id = treatment_molecule.molecule_id and treatment_molecule.pathology_id = pathology.id and molecule_id=" + str(1476))
    nomPat = [row[0] for row in result]
    
    result = db.engine.execute("select distinct molecules.name from molecules, pathology, treatment_molecule where molecules.id = treatment_molecule.molecule_id and treatment_molecule.pathology_id = pathology.id and  molecule_id=" + str(1476))
    nomMol = [row[0] for row in result]

    result = db.engine.execute("select nb_prise_jour from medication, prescription where medication.id = prescription.id_medication and prescription.id = " + str(1))
    posoT = [row[0] for row in result]

    result = db.engine.execute("select nb_comprime_prise from medication, prescription where medication.id = prescription.id_medication and prescription.id = " + str(1))
    posoNb = [row[0] for row in result]

    result = db.engine.execute("select pathology.name from  pathology, prescription where pathology.id = prescription.pathology_id and prescription.id = " + str(1))
    patolo = [row[0] for row in result]

    result = db.engine.execute("select nb_jours from medication, prescription where medication.id = prescription.id_medication and prescription.id = " + str(1))
    nbJ = [row[0] for row in result]


    

    return render_template("select.html", name="Ynov", molMed=molMed, patMol=patMol, molCla=molCla, nomPat=nomPat, nomMol=nomMol, posoT=posoT, posoNb=posoNb, patolo=patolo, nbJ=nbJ )

@app.route('/ordonnance', methods=["GET"])
def posology():
    return render_template("ordonnance.html", query=s, name="Ynov")
>>>>>>> bea0fd0ef8e9ce23d1402e74d41dd7af0f90c994

@app.route('/medicaments', methods=["GET","POST"])
def medicaments():

    return render_template("medicaments.html", name="Ynov")





