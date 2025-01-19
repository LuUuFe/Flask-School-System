from flask import render_template, redirect, url_for, flash
from app import db
from app.Models.Discipline import Discipline
from app.Models.TeacherDiscipline import TeacherDiscipline
from app.Models.DisciplineCourse import DisciplineCourse
from app.Forms.DisciplineForm import DisciplineForm
from itertools import zip_longest


def discipline():
    form = DisciplineForm()

    if form.validate_on_submit():
        name = form.name.data
        code = form.code.data
        workload = form.workload.data
        list_teacher_id = form.teacher.data
        list_course_id = form.course.data

        newDiscipline = Discipline(name=name, code=code, workload=workload)

        db.session.add(newDiscipline)

        db.session.flush()

        for teacher_id, course_id in zip_longest(
            list_teacher_id, list_course_id, fillvalue=0
        ):
            if teacher_id != 0:
                newTeacherDiscipline = TeacherDiscipline(
                    teacher_id=teacher_id, discipline_id=newDiscipline.id
                )
                db.session.add(newTeacherDiscipline)

            if course_id != 0:
                newDisciplineCourse = DisciplineCourse(
                    discipline_id=newDiscipline.id, course_id=course_id
                )
                db.session.add(newDisciplineCourse)

        db.session.commit()

        flash("Discipline registered successfully!", "success")

        return redirect(url_for("main.discipline"))

    disciplines = (
        Discipline.query.outerjoin(
            TeacherDiscipline, Discipline.id == TeacherDiscipline.discipline_id
        )
        .outerjoin(DisciplineCourse, Discipline.id == DisciplineCourse.discipline_id)
        .all()
    )

    return render_template("pages/discipline.html", form=form, disciplines=disciplines)
