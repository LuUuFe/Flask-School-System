from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import Student, Teacher, Discipline, Course, TeacherDiscipline, TeacherCourse, DisciplineCourse
from app.forms import StudentForm, TeacherForm, DisciplineForm, CourseForm
from itertools import zip_longest

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
    course_id = form.course.data

    newStudent = Student(
      name=name, 
      registration=registration, 
      date_of_birth=date_of_birth, 
      gender=gender, 
      address=address, 
      phone=phone, 
      email=email,
      course_id=course_id
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
    list_discipline_id = form.discipline.data
    list_course_id = form.course.data

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

    for discipline_id, course_id in zip_longest(list_discipline_id, list_course_id, fillvalue=0):
      if discipline_id != 0:
        newTeacherDiscipline = TeacherDiscipline(
          teacher_id=newTeacher.id,
          discipline_id=discipline_id
        )
        db.session.add(newTeacherDiscipline)

      if course_id != 0:
        newTeacherCourse = TeacherCourse(
          teacher_id=newTeacher.id,
          course_id=course_id
        )
        db.session.add(newTeacherCourse)
    
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
    list_teacher_id = form.teacher.data
    list_course_id = form.course.data

    newDiscipline = Discipline(
      name=name,
      code=code,
      workload=workload
    )

    db.session.add(newDiscipline)

    db.session.flush()

    for teacher_id, course_id in zip_longest(list_teacher_id, list_course_id, fillvalue=0):
      if teacher_id != 0:
        newTeacherDiscipline = TeacherDiscipline(
          teacher_id=teacher_id,
          discipline_id=newDiscipline.id
        )
        db.session.add(newTeacherDiscipline)

      if course_id != 0:
        newDisciplineCourse = DisciplineCourse(
          discipline_id=newDiscipline.id,
          course_id=course_id
        )
        db.session.add(newDisciplineCourse)

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
    list_student_id=form.student.data
    list_teacher_id=form.teacher.data
    list_discipline_id=form.discipline.data

    newCourse = Course(
      name=name,
      code=code
    )

    db.session.add(newCourse)

    db.session.flush()

    for student_id, teacher_id, discipline_id in zip_longest(list_student_id, list_teacher_id, list_discipline_id, fillvalue=0):
      if student_id != 0:
        updateStudent = Student.query.get_or_404(student_id)
        updateStudent.course_id = newCourse.id
        db.session.add(updateStudent)

      if teacher_id != 0:
        newTeacherCourse = TeacherCourse(
          teacher_id=teacher_id,
          course_id=newCourse.id
        )
        db.session.add(newTeacherCourse)

      if discipline_id != 0:
        newDisciplineCourse = DisciplineCourse(
          discipline_id=discipline_id,
          course_id=newCourse.id
        )
        db.session.add(newDisciplineCourse)

    db.session.commit()

    flash('Course registered successfully!', 'success')

    return redirect(url_for('main.course'))

  courses = Course.query.all()
  return render_template('course.html', form=form, courses=courses)