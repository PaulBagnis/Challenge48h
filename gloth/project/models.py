from flask_sqlalchemy import SQLAlchemy
from .views import app
import datetime

db = SQLAlchemy(app)


class ChronicDiseases(db.Model):
    __tablename__ = "chronic_diseases"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    pathology_name = db.Column(db.String(100), nullable=False)
    is_chronic = db.Column(db.Boolean, nullable=True, default=False)
    icd_10 = db.Column(db.Integer, db.ForeignKey('pathology.id', ondelete='CASCADE'))

    def __init__(self, icd_10, pathology_name, is_chronic):
        self.icd_10 = icd_10
        self.pathology_name = pathology_name
        self.is_chronic = is_chronic

    def __repr__(self):
        return "<Chronic_diseases(icd_10=%s, pathology_name=%s, is_chronic=%d)>" % (
            self.icd_10, self.pathology_name, self.is_chronic)


class Classes(db.Model):
    __tablename__ = "classes"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(200), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Classes(name=%s)>" % self.name


class ClassesFamilies(db.Model):
    __tablename__ = 'classes_families'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    atc = db.Column(db.String(200), unique=True, nullable=True)
    family_name = db.Column(db.String(200), unique=True, nullable=True)
    molecule_id = db.Column(db.Integer, db.ForeignKey('molecules.id', ondelete='CASCADE'))
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id', ondelete='CASCADE'))


class Dermocorticoids(db.Model):
    __tablename__ = "dermocorticoids"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    cis = db.Column(db.Integer, nullable=False, unique=True)
    medication_name = db.Column(db.String(), nullable=False)
    potency = db.Column(db.String(), nullable=False)

    def __init__(self, cis, medication_name, potency):
        self.cis = cis
        self.medication_name = medication_name
        self.potency = potency

    def __repr__(self):
        return "<Dermocorticoids(cis=%d,medication_name=%s,potency=%s)>" % (
            self.cis, self.medication_name, self.potency)


class Forms(db.Model):
    __tablename__ = "forms"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Forms(name=%s)>" % self.name


class Medication(db.Model):
    __tablename__ = "medication"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    molecule_id = db.Column(db.Integer, nullable=True)
    cis = db.Column(db.Integer, db.ForeignKey('dermocorticoids.id', ondelete='CASCADE'))
    name = db.Column(db.String(), nullable=False)

    def __init__(self, name, cis):
        self.molecule_id = molecule_id
        self.cis = cis
        self.name = name

    def __repr__(self):
        return "<Medication(molecule_id=%s,cis=%d,name=%s)>" % (self.molecule_id, self.cis, self.name)


class MedicationsForms(db.Model):
    __tablename__ = 'medications_forms'
    cis = db.Column(db.Integer, primary_key=True, nullable=False)
    medication_name = db.Column(db.String(200), nullable=False)
    form_name = db.Column(db.String(100), nullable=False)
    form_id = db.Column(db.Integer, db.ForeignKey('form.id', ondelete='CASCADE'))

    def __init__(self, cis, medication_name, form_name, form_id):
        self.cis = cis
        self.medication_name = medication_name
        self.form_name = form_name
        self.form_id = form_id

    def __repr__(self):
        return "<Medications_forms(cis=%d,medication_name=%s,form_name=%s,form_id=%d)>" % (
            self.cis, self.medication_name, self.form_name, self.form_id)


class Molecules(db.Model):
    __tablename__ = "molecules"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    rcp = db.Column(db.String(100), unique=True, nullable=True)
    rcp_sum = db.Column(db.String(50), nullable=True)

    def __init__(self, name, rcp):
        self.name = name
        self.rcp = rcp

    def __repr__(self):
        return "<Molecules(name=%s,rcp=%s)>" % (self.name, self.rcp)


class Opiates(db.Model):
    __tablename__ = "opiates"

    potency = db.Column(db.String(), nullable=True)
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    molecule_id = db.Column(db.Integer, db.ForeignKey('molecules.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, potency):
        self.potency = potency

    def __repr__(self):
        return "<Opiates(potency=%s)>" % self.potency


class Pathology(db.Model):
    __tablename__ = "pathology"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    info = db.Column(db.String(), nullable=False)
    has = db.Column(db.String(), nullable=True)
    age_min = db.Column(db.Integer, nullable=False)
    age_max = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(), nullable=False)
    symptoms = db.Column(db.String(), nullable=False)
    other_name = db.Column(db.String(), nullable=True)
    norm_name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    icd_10 = db.Column(db.String(), nullable=False)
    rec_tests_string = db.Column(db.String(), nullable=True)
    rec_tests = db.Column(db.PickleType, nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now(tz=app.config['TIMEZONE']))
    updated_by = db.Column(db.Integer, nullable=True)
    updated_on = db.Column(db.DateTime, server_default=db.func.now(tz=app.config['TIMEZONE']))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    treatment = db.Column(db.String(), nullable=True)
    specialty = db.relationship('Specialty', secondary='pathology_specialty')

    def __init__(self, name, info, symptoms, age_min, age_max, sex, user_id, rec_tests=[], has=None,
                 other_name=None, rec_tests_string="", updated_by=None, updated_on=None, treatment=None,
                 description=None, icd_10=None):
        self.name = name
        self.info = info
        self.age_min = age_min
        self.age_max = age_max
        self.sex = sex
        self.has = has
        self.description = description
        self.icd_10 = icd_10
        self.symptoms = symptoms
        self.other_name = other_name
        self.rec_tests = rec_tests
        self.rec_tests_string = rec_tests_string
        self.norm_name = pt.strip_accents(name.lower().strip())
        self.user_id = user_id
        self.updated_by = updated_by
        self.updated_on = updated_on
        self.treatment = treatment

    def __repr__(self):
        return "<Pathology(pathology=%s)>" % self.name

    def __str__(self):
        return self.name


class PathologySpecialty(db.Model):
    """
    Interface between pathology and specialty
    """
    __tablename__ = 'pathology_specialty'
    id = db.Column(db.Integer, primary_key=True)
    pathology_id = db.Column(db.Integer, db.ForeignKey('pathology.id', ondelete='CASCADE'))
    specialty_id = db.Column(db.Integer, db.ForeignKey('specialty.id', ondelete='CASCADE'))


class Patient(db.Model):
    __tablename__ = "patient"
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    symptoms = db.Column(db.String(), nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    tests = db.Column(db.String(), nullable=True)
    rec_tests = db.Column(db.String(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    pathology_id = db.Column(db.Integer, db.ForeignKey('pathology.id', ondelete='CASCADE'), nullable=False)
    pathology_name = db.Column(db.String(), nullable=False)
    updated_on = db.Column(db.DateTime, nullable=True)
    updated_by = db.Column(db.String(), nullable=True)
    icd_10 = db.Column(db.String(), nullable=False)

    def __init__(self, age, sex, weight, height, symptoms, user_id, pathology_id, pathology_name, icd_10):
        self.age = age
        self.sex = sex
        self.weight = weight
        self.height = height
        self.symptoms = symptoms
        self.bmi = weight / (height ** 2)
        self.user_id = user_id
        self.created_on = datetime.now()
        self.pathology_id = pathology_id
        self.pathology_name = pathology_name
        self.icd_10 = icd_10


class Roles(db.Model):
    """
    Define user roles
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Role(name=%s)>" % self.name


class Specialty(db.Model):
    """
    Define pathology specialty
    """
    __tablename__ = "specialty"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return "<Specialty(name=%s)>" % (self.name)


class Thesaurus(db.Model):
    __tablename__ = "thesaurus"

    id = db.Column(db.Integer, primary_key=True)
    molecule_id_1 = db.Column(db.Integer, db.ForeignKey('molecule.id', ondelete='CASCADE'), nullable=False)
    molecule_id_2 = db.Column(db.Integer, db.ForeignKey('molecule.id', ondelete='CASCADE'), nullable=False)
    remark = db.Column(db.String(), nullable=True)
    interaction_level = db.Column(db.String(), nullable=False)
    cis = db.Column(db.Integer, nullable=False)

    def __init__(self, molecule_id_1, molecule_id_2, remark, interaction_level, cis):
        self.molecule_id_1 = molecule_id_1
        self.molecule_id_2 = molecule_id_2
        self.remark = remark
        self.interaction_level = interaction_level

    def __str__(self):
        return "<Thesaurus(interaction_level=%s)>" % self.interaction_level


class TreatmentCis(db.Model):
    __tablename__ = "treatment_cis"

    id = db.Column(db.Integer, primary_key=True)
    pathology_id = db.Column(db.Integer, db.ForeignKey('pathology.id', ondelete='CASCADE'), nullable=False)
    pathology_name = db.Column(db.String(), nullable=False)
    medicament_id = db.Column(db.Integer, db.ForeignKey('medication.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, icd_10, pathology_name, medicament_id):
        self.icd10 = icd_10
        self.pathology_name = pathology_name
        self.medicament_id = medicament_id


class TreatmentClass(db.Model):
    __tablename__ = "treatment_class"

    id = db.Column(db.Integer, primary_key=True)
    pathology_id = db.Column(db.Integer, db.ForeignKey('pathology.id', ondelete='CASCADE'), nullable=False)
    pathology_name = db.Column(db.String(), nullable=False)
    class_id = db.Column(db.String(), nullable=True)

    def __init__(self, pathology_id, pathology_name, class_id):
        self.pathology_id = pathology_id
        self.pathology_name = pathology_name
        self.class_id = class_id


class TreatmentMolecule(db.Model):
    __tablename__ = "treatment_molecule"

    id = db.Column(db.Integer, primary_key=True)
    pathology_id = db.Column(db.Integer, db.ForeignKey('pathology.id', ondelete='CASCADE'), nullable=False)
    pathology_name = db.Column(db.String(), nullable=False)
    molecule_id = db.Column(db.Integer, db.ForeignKey('molecule.id', ondelete='CASCADE'), nullable=True)

    def __init__(self, pathology_id, pathology_name, molecule_id):
        self.pathology_id = pathology_id
        self.pathology_name = pathology_name
        self.molecule_id = molecule_id


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    rpps = db.Column(db.BigInteger, unique=True)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    forename = db.Column(db.String(50), nullable=False)
    registered_on = db.Column(db.DateTime, server_default=db.func.now(tz=app.config['TIMEZONE']))
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    entry_count_patient = db.Column(db.Integer, nullable=False, default=0)
    entry_count_pathology = db.Column(db.Integer, nullable=False, default=0)
    modify_count_patient = db.Column(db.Integer, nullable=False, default=0)
    modify_count_pathology = db.Column(db.Integer, nullable=False, default=0)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    zip_code = db.Column(db.String(20), nullable=False)

    # roles = db.relationship('Role', secondary='user_roles')

    def __init__(self, name, forename, rpps, email, password, confirmed=True, confirmed_on=None, entry_count_patient=0,
                 entry_count_pathology=0, modify_count_patient=0, modify_count_pathology=0, phone=0, zip_code=0):
        self.rpps = rpps
        self.password = password
        self.email = email
        self.forename = forename
        self.name = name
        self.confirmed_on = confirmed_on
        self.confirmed = confirmed
        self.entry_count_patient = entry_count_patient
        self.entry_count_pathology = entry_count_pathology
        self.modify_count_patient = modify_count_patient
        self.modify_count_pathology = modify_count_pathology
        self.phone = phone
        self.zip_code = zip_code

    def __repr__(self):
        return "<User(forename=%s, name=%s, rpps=%d, email=%s)>" % (self.forename, self.name, self.rpps, self.email)


class UserRoles(db.Model):
    """
    Interface between user and roles
    """
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))
