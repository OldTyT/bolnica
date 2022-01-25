from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms_alchemy import PhoneNumberField

class reg_call(FlaskForm):
    ward = StringField('ward', validators=[DataRequired()])
    bed = StringField('bed', validators=[DataRequired()])
    date = StringField('date', validators=[DataRequired()])
    coment = StringField('coment')
    submit = SubmitField('Sign In')