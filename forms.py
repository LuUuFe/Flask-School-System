from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
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

class TeacherForm(FlaskForm):
  name = StringField('Enter your name', validators=[DataRequired()])
  registration = StringField('Enter your registration', validators=[DataRequired()])
  dateOfBirth = DateField('Enter your date of birth', format='%Y-%m-%d', validators=[DataRequired()])
  gender = StringField('Enter your gender', validators=[DataRequired()])
  address = StringField('Enter your address', validators=[DataRequired()])
  phone = StringField('Enter your phone', validators=[DataRequired()])
  email = StringField('Enter your email', validators=[DataRequired()])
  discipline = SelectField('Choose a discipline', coerce=int, validators=[DataRequired()])
  submit = SubmitField('Submit')

class DisciplineForm(FlaskForm):
  name = StringField('Enter a name', validators=[DataRequired()])
  code = StringField('Enter a code', validators=[DataRequired()])
  workload = StringField('Enter a workload', validators=[DataRequired()])
  teacher = SelectField('Choose a teacher', coerce=int, validators=[DataRequired()])
  submit = SubmitField('Submit')

class ClassForm(FlaskForm):
  name = StringField('Enter a name', validators=[DataRequired()])
  code = StringField('Enter a code', validators=[DataRequired()])
  discipline = SelectField('Choose a discipline', coerce=int, validators=[DataRequired()])
  teacher = SelectField('Choose a teacher', coerce=int, validators=[DataRequired()])
  submit = SubmitField('Submit')