from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired
from app.models import Teacher

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
  teacher = SelectField('Choose a teacher', coerce=int, default=None)
  submit = SubmitField('Submit')

  def __init__(self, *args, **kwargs):
    super(DisciplineForm, self).__init__(*args, **kwargs)
    self.teacher.choices = [(teacher.id, teacher.name) for teacher in Teacher.query.all()]
    self.teacher.choices.insert(0, (None, "No teacher"))

class ClassForm(FlaskForm):
  name = StringField('Enter a name', validators=[DataRequired()])
  code = StringField('Enter a code', validators=[DataRequired()])
  discipline = SelectField('Choose a discipline', coerce=int, validators=[DataRequired()])
  teacher = SelectField('Choose a teacher', coerce=int, validators=[DataRequired()])
  submit = SubmitField('Submit')