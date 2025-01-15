from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from app.models import Teacher, Discipline, Student, Course

class StudentForm(FlaskForm):
  name = StringField('Enter your name', validators=[DataRequired()])
  registration = StringField('Enter your registration', validators=[DataRequired()])
  dateOfBirth = DateField('Enter your date of birth', format='%Y-%m-%d', validators=[DataRequired()])
  gender = StringField('Enter your gender', validators=[DataRequired()])
  address = StringField('Enter your address', validators=[DataRequired()])
  phone = StringField('Enter your phone', validators=[DataRequired()])
  email = StringField('Enter your email', validators=[DataRequired()])
  course = SelectField('Choose a course', default=None, coerce=int)
  submit = SubmitField('Submit')

  def __init__(self, *args, **kwargs):
    super(StudentForm, self).__init__(*args, **kwargs)
    self.course.choices = [(course.id, course.name) for course in Course.query.all()]
    self.course.choices.insert(0, (0, 'No course'))

class TeacherForm(FlaskForm):
  name = StringField('Enter your name', validators=[DataRequired()])
  registration = StringField('Enter your registration', validators=[DataRequired()])
  dateOfBirth = DateField('Enter your date of birth', format='%Y-%m-%d', validators=[DataRequired()])
  gender = StringField('Enter your gender', validators=[DataRequired()])
  address = StringField('Enter your address', validators=[DataRequired()])
  phone = StringField('Enter your phone', validators=[DataRequired()])
  email = StringField('Enter your email', validators=[DataRequired()])
  discipline = SelectMultipleField('Choose a discipline', default=None, coerce=int)
  course = SelectMultipleField('Choose a course', default=None, coerce=int)
  submit = SubmitField('Submit')  

  def __init__(self, *args, **kwargs):
    super(TeacherForm, self).__init__(*args, **kwargs)
    self.discipline.choices = [(discipline.id, discipline.name) for discipline in Discipline.query.all()]
    self.discipline.choices.insert(0, (0, 'No discipline'))
    self.course.choices = [(course.id, course.name) for course in Course.query.all()]
    self.course.choices.insert(0, (0, 'No course'))

class DisciplineForm(FlaskForm):
  name = StringField('Enter a name', validators=[DataRequired()])
  code = StringField('Enter a code', validators=[DataRequired()])
  workload = StringField('Enter a workload', validators=[DataRequired()])
  teacher = SelectMultipleField('Choose a teacher', coerce=int, default=None)
  course = SelectMultipleField('Choose a course', coerce=int, default=None)
  submit = SubmitField('Submit')

  def __init__(self, *args, **kwargs):
    super(DisciplineForm, self).__init__(*args, **kwargs)
    self.teacher.choices = [(teacher.id, teacher.name) for teacher in Teacher.query.all()]
    self.teacher.choices.insert(0, (0, 'No teacher'))
    self.course.choices = [(course.id, course.name) for course in Course.query.all()]
    self.course.choices.insert(0, (0, 'No course'))

class CourseForm(FlaskForm):
  name = StringField('Enter a name', validators=[DataRequired()])
  code = StringField('Enter a code', validators=[DataRequired()])
  student = SelectMultipleField('Choose a student', default=None, coerce=int)
  teacher = SelectMultipleField('Choose a teacher', default=None, coerce=int)
  discipline = SelectMultipleField('Choose a discipline', default=None, coerce=int)
  submit = SubmitField('Submit')

  def __init__(self, *args, **kwargs):
    super(CourseForm, self).__init__(*args, **kwargs)
    self.student.choices = [(student.id, student.name) for student in Student.query.all()]
    self.student.choices.insert(0, (0, 'No student'))
    self.teacher.choices = [(teacher.id, teacher.name) for teacher in Teacher.query.all()]
    self.teacher.choices.insert(0, (0, 'No teacher'))
    self.discipline.choices = [(discipline.id, discipline.name) for discipline in Discipline.query.all()]
    self.discipline.choices.insert(0, (0, 'No discipline'))
