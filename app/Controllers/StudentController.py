from flask import render_template, redirect, url_for, flash
from app import db
from app.Models.Student import Student
from app.Models.Course import Course
from app.Forms.StudentForm import StudentForm


def student():
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
    return render_template("pages/student.html", form=form, students=students)
