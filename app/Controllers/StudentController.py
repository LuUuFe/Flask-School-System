from flask import render_template, redirect, url_for, flash
from app import db
from app.Models.Student import Student
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
        # Create a dictionary with the form data
        studentData = {
            "name": form.name.data,
            "registration": form.registration.data,
            "date_of_birth": datetime.strftime(form.dateOfBirth.data, "%d/%m/%Y"), # Convert datetime object to string
            "gender": "Male" if form.gender.data == 1 else "Female", # Convert radio button value to string
            "address": form.address.data,
            "phone": form.phone.data,
            "email": form.email.data,
            "course_id": form.course.data,
        }

        # Create a new Student object and add it to the database
        newStudent = Student(**studentData)
        db.session.add(newStudent)
        db.session.commit()

        # Flash a success message and redirect to this route
        flash("Student registered successfully!", "success")
        return redirect(url_for("main.student"))

    # Get all students from the database
    students = Student.query.all()

    # Render the student.html template with the registration form and all students
    return render_template("pages/student/index.html", form=form, students=students)


def edit(id):
    """
    Handles the student edit form and updates a student in the database.

    :param id: The ID of the student to edit
    :return: A rendered template with the edit form and all students if the form is invalid,
             otherwise a redirect to the student list page
    """
    student = Student.query.get_or_404(id)

    form = StudentForm(obj=student)

    if form.validate_on_submit():
        # Update the student object with the form data
        student.name = form.name.data
        student.registration = form.registration.data
        student.date_of_birth = datetime.strftime(form.dateOfBirth.data, "%d/%m/%Y")
        student.gender = "Male" if form.gender.data == 1 else "Female"
        student.address = form.address.data
        student.phone = form.phone.data
        student.email = form.email.data
        student.course_id = form.course.data

        # Commit the changes to the database
        db.session.commit()

        # Flash a success message and redirect to the student list page
        flash(f"Student {student.name} updated successfully!", "success")
        return redirect(url_for("main.student"))

    # Populate the form with the student data
    form.populate_obj(student)

    # Populate the gender radio field with the student's gender
    form.gender.data = 1 if student.gender == "Male" else 2

    # Populate the course select field with the student's course
    form.course.data = student.course_id

    # Convert the date string to a datetime object for the date of birth field
    form.dateOfBirth.data = datetime.strptime(student.date_of_birth, "%d/%m/%Y")

    # Render the edit template with the form and student data
    return render_template("pages/student/edit.html", form=form, student=student)


def destroy(id):
    """
    Deletes a student from the database.

    :param id: The ID of the student to delete
    :return: A redirect to the student list page
    """
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash(f"Student {student.name} deleted successfully!", "success")
    return redirect(url_for("main.student"))
