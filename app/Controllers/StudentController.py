from flask import render_template, redirect, url_for, flash, request
from app import db
from app.Models.Student import Student
from app.Forms.StudentForm import StudentForm
from datetime import datetime


def index():
    """
    Renders the student registration form and displays all registered students in a table.

    :return: A rendered template with the registration form and all students
    """

    # Get all students from the database
    students = Student.query.all()

    # Render the student.html template with the registration form and all students
    return render_template("pages/student/index.html", students=students)


def create():
    """
    Handles the student registration form and adds a new student to the database.

    If the form is valid, it creates a new Student object and adds it to the database.
    After successful registration, it flashes a success message and redirects to this route.

    Otherwise, it renders the create.html template with the registration form and all students.
    """

    # Create a form object for the student registration form
    form = StudentForm()

    if form.validate_on_submit():
        # Create a dictionary with the form data
        studentData = {
            "name": form.name.data,
            "registration": form.registration.data,
            "date_of_birth": datetime.strftime(
                form.dateOfBirth.data, "%d/%m/%Y"
            ),  # Convert datetime object to string
            "gender": (
                "Male" if form.gender.data == 1 else "Female"
            ),  # Convert radio button value to string
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

    # Render the create.html template with the registration form, but do not store it in the browsing history
    return render_template("pages/student/create.html", form=form)


def edit(id: int):
    """
    Handles the student edit form and updates a student in the database.

    If the form is valid, it updates the student object and commits the changes to the database.
    After successful update, it flashes a success message and redirects to the student list page.

    Otherwise, it renders the student.html template with the edit form and all students.
    """

    # Retrieve the student object from the database or return a 404 error if not found
    student = Student.query.get_or_404(id)

    # Instantiate the form with the student object
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

    # Populate the gender radio field with the student's gender
    form.gender.data = 1 if student.gender == "Male" else 2

    # Populate the course select field with the student's course
    form.course.data = student.course_id

    # Convert the date string to a datetime object for the date of birth field
    form.dateOfBirth.data = datetime.strptime(student.date_of_birth, "%d/%m/%Y")

    # Render the edit template with the form and student data
    return render_template("pages/student/edit.html", form=form, student=student)


def destroy(id: int):
    """
    Deletes a student from the database.

    Retrieves the student object from the database or returns a 404 error if not found.
    Deletes the student object from the database and commits the changes.
    Flashes a success message with the student's name and redirects to the student list page.

    :param id: The ID of the student to delete
    :return: A redirect to the student list page
    """
    # Retrieve the student object from the database or return a 404 error if not found
    student = Student.query.get_or_404(id)

    # Delete the student object from the database and commit the changes
    db.session.delete(student)
    db.session.commit()

    # Flash a success message with the student's name and redirect to the student list page
    flash(f"Student {student.name} deleted successfully!", "success")
    return redirect(url_for("main.student"))
