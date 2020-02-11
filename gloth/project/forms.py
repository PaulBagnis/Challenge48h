from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, BooleanField, TextAreaField, StringField
from wtforms import PasswordField, DecimalField
from wtforms_components import IntegerField
from wtforms.fields.html5 import EmailField, DateTimeLocalField
from wtforms import validators
from .utils import pathologyChoices, userChoices

class PatientForm(FlaskForm):
    pathology = SelectField("Pathologie", validators = [validators.InputRequired()], id = "pathology", choices = pathologyChoices())
    user = SelectField("Docteur", validators = [validators.InputRequired()], id = "user", choices = userChoices())
    submit = SubmitField("Valider")

class MedicForm(FlaskForm):
    submit = SubmitField("Valider")

class PosologyForm(FlaskForm):
    comprime = SelectField("COMPRIMÉ PAR PRISE", validators = [validators.InputRequired()], id = "pathology", choices = pathologyChoices())
    prise = SelectField("PRISE PAR JOUR", validators = [validators.InputRequired()], id = "user", choices = userChoices())
    duree = SelectField("DURÉE DU TRAITEMENT", validators = [validators.InputRequired()], id = "user", choices = userChoices())
    submit = SubmitField("Valider")



