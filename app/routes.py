from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import Student, Teacher, Discipline, Course, TeacherDiscipline
from app.forms import StudentForm, TeacherForm, DisciplineForm, CourseForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@main.route('/student', methods=['GET', 'POST'])
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

    return redirect(url_for('main.student'))
  
  students = Student.query.all()
  return render_template('student.html', form=form, students=students)

@main.route('/teacher', methods=['GET', 'POST'])
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
    discipline_id = form.discipline.data

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

    db.session.flush()

    newTeacherDiscipline = TeacherDiscipline(
      teacher_id=newTeacher.id,
      discipline_id=discipline_id
    )

    db.session.add(newTeacherDiscipline)

    db.session.commit()

    flash('Teacher registered successfully!', 'success')

    return redirect(url_for('main.teacher'))

  teachers = Teacher.query.all()
  return render_template('teacher.html', form=form, teachers=teachers)

@main.route('/discipline', methods=['GET', 'POST'])
def discipline():
  form = DisciplineForm()

  if form.validate_on_submit():
    name = form.name.data
    code = form.code.data
    workload = form.workload.data
    teacher_id = form.teacher.data

    newDiscipline = Discipline(
      name=name,
      code=code,
      workload=workload
    )

    db.session.add(newDiscipline)

    db.session.flush()

    newTeacherDiscipline = TeacherDiscipline(
      teacher_id=teacher_id,
      discipline_id=newDiscipline.id
    )

    db.session.add(newTeacherDiscipline)

    db.session.commit()

    flash('Discipline registered successfully!', 'success')

    return redirect(url_for('main.discipline'))

  disciplines = Discipline.query.all()
  return render_template('discipline.html', form=form, disciplines=disciplines)

@main.route('/course', methods=['GET', 'POST'])
def course():
  form = CourseForm()

  if form.validate_on_submit():
    name = form.name.data
    code = form.code.data
    discipline_id = form.discipline.data
    teacher_id = form.teacher.data

    newCourse = Course(
      name=name,
      code=code,
      discipline_id=discipline_id,
      teacher_id=teacher_id
    )

    db.session.add(newCourse)
    db.session.commit()

    flash('Course registered successfully!', 'success')

    return redirect(url_for('main.course'))

  courses = Course.query.all()
  return render_template('course.html', form=form, courses=courses)