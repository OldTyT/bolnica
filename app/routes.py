# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from app import app, db
from app.models import *
from app.forms import reg_call

@app.route('/')
@app.route('/index')
def index():
    return('Hello, world')

@app.route('/good')
def good():
    return('Форму принял!')

@app.route('/call', methods=['GET', 'POST'])
def call():
    form = reg_call()
    if form.validate_on_submit():
        db.session.add(Patient(ward=form.ward.data, bed=form.bed.data, date=form.date.data, coment=form.coment.data))
        db.session.commit()
        return redirect('/good')
    return render_template('login.html', form=form)