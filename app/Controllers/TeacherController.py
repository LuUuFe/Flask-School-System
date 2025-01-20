from ast import dump
from flask import render_template, redirect, url_for, flash
from app import db
from app.Models.Teacher import Teacher
from app.Models.TeacherDiscipline import TeacherDiscipline
from app.Models.TeacherCourse import TeacherCourse
from app.Forms.TeacherForm import TeacherForm
from itertools import zip_longest
from datetime import datetime


def teacher():
    """Handles the teacher registration form and displays all teachers in the database."""

    form = TeacherForm()

    if form.validate_on_submit():
        newTeacher = {
            "name": form.name.data,
            "registration": form.registration.data,
            "date_of_birth": datetime.strftime(form.dateOfBirth.data, "%d/%m/%Y"),
            "gender": "Male" if form.gender.data == 1 else "Female",
            "address": form.address.data,
            "phone": form.phone.data,
            "email": form.email.data,
        }

        # Create a new Teacher object and add it to the database
        newTeacher = Teacher(**newTeacher)
        db.session.add(newTeacher)
        db.session.flush()

        add_data_from_related_tables(form, newTeacher)

        db.session.commit()

        flash("Teacher registered successfully!", "success")

        return redirect(url_for("main.teacher"))

    teachers = Teacher.query.all()

    return render_template("pages/teacher/index.html", form=form, teachers=teachers)


def edit(id):
    """
    Handles the teacher edit form and updates a teacher in the database.

    If the form is valid, it updates the teacher object and adds or removes disciplines and courses
    from the teacher. After successful update, it flashes a success message and redirects to this route.

    Otherwise, it renders the teacher.html template with the edit form and all teachers.
    """
    teacher = Teacher.query.get_or_404(id)

    form = TeacherForm(obj=teacher)

    if form.validate_on_submit():
        teacher.name = form.name.data
        teacher.registration = form.registration.data
        teacher.date_of_birth = datetime.strftime(form.dateOfBirth.data, "%d/%m/%Y")
        teacher.gender = "Male" if form.gender.data == 1 else "Female"
        teacher.address = form.address.data
        teacher.phone = form.phone.data
        teacher.email = form.email.data


        add_data_from_related_tables(form, teacher)

        db.session.commit()

        flash(f"Teacher {teacher.name} updated successfully!", "success")

        return redirect(url_for("main.teacher"))

    form.populate_obj(teacher)

    # Convert the date string to a datetime object
    form.dateOfBirth.data = datetime.strptime(teacher.date_of_birth, "%d/%m/%Y")

    form.gender.data = 1 if teacher.gender == "Male" else 2

    form.discipline.data = [discipline.id for discipline in teacher.disciplines]
    form.course.data = [course.id for course in teacher.courses]

    return render_template("pages/teacher/edit.html", form=form, teacher=teacher)


def destroy(id):
    """
    Delete a teacher from the database
    :param id: The ID of the teacher to delete
    :return: A redirect to the teacher list page
    """
    teacher = Teacher.query.get_or_404(id)
    db.session.delete(teacher)
    db.session.commit()
    flash(f"Teacher {teacher.name} deleted successfully!", "success")
    return redirect(url_for("main.teacher"))


def add_data_from_related_tables(form, teacher):
    """
    Add or remove the disciplines and courses selected in the form to/from the teacher in the database
    :param form: The form containing the selected disciplines and courses
    :param teacher: The teacher to add or remove the disciplines and courses to/from
    :return: None
    """

    # Clear existing relationships
    TeacherDiscipline.query.filter_by(teacher_id=teacher.id).delete()
    TeacherCourse.query.filter_by(teacher_id=teacher.id).delete()

    # Add new relationships based on form data
    for disciplineId, courseId in zip_longest(
        form.discipline.data, form.course.data, fillvalue=0
    ):
        if disciplineId != 0:
            db.session.add(
                TeacherDiscipline(teacher_id=teacher.id, discipline_id=disciplineId)
            )

        if courseId != 0:
            db.session.add(TeacherCourse(teacher_id=teacher.id, course_id=courseId))
