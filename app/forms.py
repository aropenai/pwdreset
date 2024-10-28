# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class ResetForm(FlaskForm):
    email = StringField('User Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Reset Password')