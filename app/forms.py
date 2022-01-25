from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class reg_call(FlaskForm):
    ward = StringField('ward', validators=[DataRequired()])
    bed = StringField('bed', validators=[DataRequired()])
    datetime = StringField('date')
    active = StringField('active')
    comment = StringField('comment')
    submit = SubmitField('Sign In')


class admin_panel(FlaskForm):
    id = StringField('id', validators=[DataRequired()])
    update = SubmitField('Update')