from flask import render_template, redirect, url_for, flash
from app import db
from app.Models.Student import Student
from app.Models.Course import Course
from app.Forms.StudentForm import StudentForm
from datetime import datetime


def index():
    """
    Handles the student registration form and displays all students in the database.

    If the form is valid, it creates a new Student object and adds it to the database.
    After successful registration, it flashes a success message and redirects to this route.

    Otherwise, it renders the student.html template with the registration form and all students.
    """
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
            course_id=course_id,
        )

        db.session.add(newStudent)
        db.session.commit()

        flash("Student registered successfully!", "success")

        return redirect(url_for("main.student"))

    students = Student.query.outerjoin(Course, Student.course_id == Course.id).all()
    return render_template("pages/student/index.html", form=form, students=students)


def edit(id):

    student = Student.query.get_or_404(id)

    form = StudentForm()

    if form.validate_on_submit():
        student.name = form.name.data
        student.registration = form.registration.data
        student.date_of_birth = form.dateOfBirth.data
        student.gender = form.gender.data
        student.address = form.address.data
        student.phone = form.phone.data
        student.email = form.email.data
        student.course_id = form.course.data

        db.session.commit()

        flash(f"Student {student.name} updated successfully!", "success")

        return redirect(url_for("main.student"))

    form.name.data = student.name
    form.registration.data = student.registration

    # Convert the date string to a datetime object
    dateOfBirthToDatetime = datetime.strptime(student.date_of_birth, "%d/%m/%Y")
    dateOfBirthToStr = datetime.strftime(dateOfBirthToDatetime, "%Y-%m-%d")
    form.dateOfBirth.data = datetime.strptime(dateOfBirthToStr, "%Y-%m-%d")
    
    form.gender.data = student.gender
    form.address.data = student.address
    form.phone.data = student.phone
    form.email.data = student.email
    form.course.data = student.course_id

    return render_template("pages/student/edit.html", form=form, student=student)


def destroy(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash(f"Student {student.name} deleted successfully!", "success")
    return redirect(url_for("main.student"))
