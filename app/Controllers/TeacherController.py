from flask import render_template, redirect, url_for, flash
from app import db
from app.Models.Teacher import Teacher
from app.Models.TeacherDiscipline import TeacherDiscipline
from app.Models.TeacherCourse import TeacherCourse
from app.Forms.TeacherForm import TeacherForm
from itertools import zip_longest
from datetime import datetime


def teacher():
    """
    Handles the teacher registration form and displays all teachers in the database.

    If the form is valid, it creates a new Teacher object and adds it to the database.
    It also associates the teacher with selected disciplines and courses.
    After successful registration, it flashes a success message and redirects to this route.

    Otherwise, it renders the teacher.html template with the registration form and all teachers.
    """

    form = TeacherForm()

    if form.validate_on_submit():
        name = form.name.data
        registration = form.registration.data
        date_of_birth = datetime.strftime(form.dateOfBirth.data, "%d/%m/%Y")
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
            email=email,
        )

        db.session.add(newTeacher)

        db.session.flush()

        for discipline_id, course_id in zip_longest(
            list_discipline_id, list_course_id, fillvalue=0
        ):
            if discipline_id != 0:
                newTeacherDiscipline = TeacherDiscipline(
                    teacher_id=newTeacher.id, discipline_id=discipline_id
                )
                db.session.add(newTeacherDiscipline)

            if course_id != 0:
                newTeacherCourse = TeacherCourse(
                    teacher_id=newTeacher.id, course_id=course_id
                )
                db.session.add(newTeacherCourse)

        db.session.commit()

        flash("Teacher registered successfully!", "success")

        return redirect(url_for("main.teacher"))

    teachers = (
        Teacher.query.outerjoin(
            TeacherDiscipline, Teacher.id == TeacherDiscipline.teacher_id
        )
        .outerjoin(TeacherCourse, Teacher.id == TeacherCourse.teacher_id)
        .all()
    )
    return render_template("pages/teacher.html", form=form, teachers=teachers)
