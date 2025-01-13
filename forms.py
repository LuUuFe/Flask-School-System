from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
  name = StringField('Enter your name', validators=[DataRequired()])
  registration = StringField('Enter your registration', validators=[DataRequired()])
  dateOfBirth = DateField('Enter your date of birth', format='%Y-%m-%d', validators=[DataRequired()])
  gender = StringField('Enter your gender', validators=[DataRequired()])
  address = StringField('Enter your address', validators=[DataRequired()])
  phone = StringField('Enter your phone', validators=[DataRequired()])
  email = StringField('Enter your email', validators=[DataRequired()])
  submit = SubmitField('Submit')