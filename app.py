from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from forms import StudentForm

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
      email=email)

    db.session.add(newStudent)
    db.session.commit()
    
    flash('Student registered successfully!', 'success')

    return redirect(url_for('student'))
  
  students = Student.query.all()
  return render_template('student.html', form=form, students=students)

if __name__ == '__main__':
  app.run(debug=True)