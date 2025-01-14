from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from forms import StudentForm, TeacherForm, DisciplineForm, ClassForm

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

class Student(db.Model):
  __tablename__ = 'students'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  registration = db.Column(db.String(50), unique=True, nullable=False)
  date_of_birth = db.Column(db.String(20), nullable=False)
  gender = db.Column(db.String(10), nullable=False)
  address = db.Column(db.String(255), nullable=False)
  phone = db.Column(db.String(15), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)

class Teacher(db.Model):
  __tablename__ = 'teachers'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  registration = db.Column(db.String(50), unique=True, nullable=False)
  date_of_birth = db.Column(db.String(20), nullable=False)
  gender = db.Column(db.String(10), nullable=False)
  address = db.Column(db.String(255), nullable=False)
  phone = db.Column(db.String(15), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  
  disciplines = db.relationship('Discipline', backref='teacher', lazy=True)

class Discipline(db.Model):
  __tablename__ = 'disciplines'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  code = db.Column(db.String(50), unique=True, nullable=False)
  workload = db.Column(db.String(20), nullable=False)
  
  teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
  
  classes = db.relationship('Class', backref='discipline', lazy=True)

class Class(db.Model):
  __tablename__ = 'classes'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  code = db.Column(db.String(50), unique=True, nullable=False)
  
  discipline_id = db.Column(db.Integer, db.ForeignKey('disciplines.id'), nullable=False)
  
  teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)

with app.app_context():
  db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@app.route('/student', methods=['GET', 'POST'])
def student():
  form = StudentForm()
  
  if form.validate_on_submit():
    name = form.name.data
    registration = form.registration.data
    date_of_birth = form.dateOfBirth.data
    gender = form.gender.data
    address = form.address.data
    phone = form.phone.data
    email = form.email.data

    newStudent = Student(
      name=name, 
      registration=registration, 
      date_of_birth=date_of_birth, 
      gender=gender, 
      address=address, 
      phone=phone, 
      email=email
      )

    db.session.add(newStudent)
    db.session.commit()
    
    flash('Student registered successfully!', 'success')

    return redirect(url_for('student'))
  
  students = Student.query.all()
  return render_template('student.html', form=form, students=students)

@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
  form = TeacherForm()

  if form.validate_on_submit():
    name = form.name.data
    registration = form.registration.data
    date_of_birth = form.dateOfBirth.data
    gender = form.gender.data
    address = form.address.data
    phone = form.phone.data
    email = form.email.data

    newTeacher = Teacher(
      name=name,
      registration=registration,
      date_of_birth=date_of_birth,
      gender=gender,
      address=address,
      phone=phone,
      email=email
    )

    db.session.add(newTeacher)
    db.session.commit()

    flash('Teacher registered successfully!', 'success')

    return redirect(url_for('teacher'))

  teachers = Teacher.query.all()
  return render_template('teacher.html', form=form, teachers=teachers)

@app.route('/discipline', methods=['GET', 'POST'])
def discipline():
  form = DisciplineForm()
  form.teacher.choices = [(teacher.id, teacher.name) for teacher in Teacher.query.all()]

  if form.validate_on_submit():
    name = form.name.data
    code = form.code.data
    workload = form.workload.data
    teacher_id = form.teacher.data

    newDiscipline = Discipline(
      name=name,
      code=code,
      workload=workload,
      teacher_id=teacher_id
    )

    db.session.add(newDiscipline)
    db.session.commit()

    flash('Discipline registered successfully!', 'success')

    return redirect(url_for('discipline'))

  disciplines = Discipline.query.all()
  return render_template('discipline.html', form=form, disciplines=disciplines)

@app.route('/class', methods=['GET', 'POST'])
def class_():
  form = ClassForm()
  form.discipline.choices = [(discipline.id, discipline.name) for discipline in Discipline.query.all()]
  form.teacher.choices = [(teacher.id, teacher.name) for teacher in Teacher.query.all()]

  if form.validate_on_submit():
    name = form.name.data
    code = form.code.data
    discipline_id = form.discipline.data
    teacher_id = form.teacher.data

    newClass = Class(
      name=name,
      code=code,
      discipline_id=discipline_id,
      teacher_id=teacher_id
    )

    db.session.add(newClass)
    db.session.commit()

    flash('Class registered successfully!', 'success')

    return redirect(url_for('class_'))

  classes = Class.query.all()
  return render_template('class.html', form=form, classes=classes)

if __name__ == '__main__':
  app.run(debug=True)