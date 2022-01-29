# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from app import app
import json
from app.models import *
from app.forms import reg_call, admin_panel


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, world'


@app.route('/good')
def good():
    return 'Форму принял!'


@app.route('/call', methods=['GET', 'POST'])
def call():
    form = reg_call()
    if form.validate_on_submit():
        db.session.add(Patient(ward=form.ward.data, bed=form.bed.data, comment=form.comment.data))
        db.session.commit()
        return redirect('/good')
    return render_template('login.html', form=form)


@app.route('/adm', methods=['GET', 'POST'])
def adm():
    form = admin_panel()
    patients = db.session.query(Patient).all()
    if form.validate_on_submit():
        if db.session.query(Patient).filter(Patient.id == int(form.id.data)).all() != []:
            Patient_e = db.session.query(Patient).filter(Patient.id == int(form.id.data)).all()[0]
            Patient_e.active = False
            db.session.add(Patient_e)
            db.session.commit()
    return render_template('adm.html', patients=patients, form=form)

@app.route('/stat', methods=['GET', 'POST'])
def stat():
    patients = db.session.query(Patient).all()
    result = json.loads("""{"patients": []}""")
    #result['patients'].append(json.loads("""{"qwe":"qew"}"""))
    for patient in patients:
        result['patients'].append(json.loads("""{
        "id": """ + str(patient.id) + """,
        "ward": """ + str(patient.ward) + """,
        "bed": """ + str(patient.bed) + """,
        "active": """ + str(patient.active) + """
    }"""))
    return result
