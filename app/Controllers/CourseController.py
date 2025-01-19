from flask import render_template, flash, redirect, url_for
from app import db
from app.Models.Student import Student
from app.Models.TeacherCourse import TeacherCourse
from app.Models.DisciplineCourse import DisciplineCourse
from app.Models.Course import Course
from app.Forms.CourseForm import CourseForm
from itertools import zip_longest


def course():
    form = CourseForm()

    if form.validate_on_submit():
        name = form.name.data
        code = form.code.data
        list_student_id = form.student.data
        list_teacher_id = form.teacher.data
        list_discipline_id = form.discipline.data

        newCourse = Course(name=name, code=code)

        db.session.add(newCourse)

        db.session.flush()

        for student_id, teacher_id, discipline_id in zip_longest(
            list_student_id, list_teacher_id, list_discipline_id, fillvalue=0
        ):
            if student_id != 0:
                updateStudent = Student.query.get_or_404(student_id)
                updateStudent.course_id = newCourse.id
                db.session.add(updateStudent)

            if teacher_id != 0:
                newTeacherCourse = TeacherCourse(
                    teacher_id=teacher_id, course_id=newCourse.id
                )
                db.session.add(newTeacherCourse)

            if discipline_id != 0:
                newDisciplineCourse = DisciplineCourse(
                    discipline_id=discipline_id, course_id=newCourse.id
                )
                db.session.add(newDisciplineCourse)

        db.session.commit()

        flash("Course registered successfully!", "success")

        return redirect(url_for("main.course"))

    courses = (
        Course.query.outerjoin(TeacherCourse, Course.id == TeacherCourse.course_id)
        .outerjoin(DisciplineCourse, Course.id == DisciplineCourse.course_id)
        .outerjoin(Student, Course.id == Student.course_id)
    )
    return render_template("pages/course.html", form=form, courses=courses)
