from flask import render_template, flash, redirect, url_for
from app import db
from app.Models.Student import Student
from app.Models.TeacherCourse import TeacherCourse
from app.Models.DisciplineCourse import DisciplineCourse
from app.Models.Course import Course
from app.Forms.CourseForm import CourseForm
from itertools import zip_longest


def index():
    form = CourseForm()

    if form.validate_on_submit():
        name = form.name.data
        code = form.code.data

        newCourse = Course(name=name, code=code)

        db.session.add(newCourse)

        db.session.flush()

        add_data_from_related_tables(form, newCourse)

        db.session.commit()

        flash("Course registered successfully!", "success")

        return redirect(url_for("main.course"))

    courses = Course.query.all()

    return render_template("pages/course/index.html", form=form, courses=courses)


def edit(id):
    course = Course.query.get_or_404(id)

    form = CourseForm(obj=course)

    if form.validate_on_submit():
        course.name = form.name.data
        course.code = form.code.data
        course.workload = form.workload.data

        add_data_from_related_tables(form, course)

        db.session.commit()

        flash(f"Course {course.name} updated successfully!", "success")

        return redirect(url_for("main.course"))

    form.populate_obj(course)

    form.student.data = [student.id for student in course.students]
    form.teacher.data = [teacher.id for teacher in course.teachers]
    form.discipline.data = [discipline.id for discipline in course.disciplines]

    return render_template("pages/course/edit.html", form=form, course=course)


def destroy(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    flash(f"Course {course.name} deleted successfully!", "success")
    return redirect(url_for("main.course"))


def add_data_from_related_tables(form, course):
    """
    Update the relationships of a course with students, teachers, and disciplines
    based on the provided form data. Existing relationships are cleared before
    adding the new ones.

    :param form: The form containing the new student, teacher, and discipline data.
    :param course: The course whose relationships need to be updated.
    :return: None
    """

    # Clear existing relationships
    Student.query.filter_by(course_id=course.id).delete()
    TeacherCourse.query.filter_by(course_id=course.id).delete()
    DisciplineCourse.query.filter_by(course_id=course.id).delete()

    # Add new relationships based on form data
    for studentId, teacherId, disicplineId in zip_longest(
        form.student.data, form.teacher.data, form.discipline.data, fillvalue=0
    ):
        if studentId != 0:
            db.session.add(Student(course_id=course.id))

        if teacherId != 0:
            db.session.add(TeacherCourse(teacher_id=teacherId, course_id=course.id))

        if disicplineId != 0:
            db.session.add(
                DisciplineCourse(discipline_id=disicplineId, course_id=course.id)
            )
