from flask import render_template, redirect, url_for, flash
from app import db
from app.Models.Discipline import Discipline
from app.Models.TeacherDiscipline import TeacherDiscipline
from app.Models.DisciplineCourse import DisciplineCourse
from app.Forms.DisciplineForm import DisciplineForm
from itertools import zip_longest


def index():
    form = DisciplineForm()

    if form.validate_on_submit():
        newDiscipline = Discipline(
            name=form.name.data, code=form.code.data, workload=form.workload.data
        )

        db.session.add(newDiscipline)

        db.session.flush()

        add_data_from_related_tables(form, newDiscipline)

        db.session.commit()

        flash("Discipline registered successfully!", "success")

        return redirect(url_for("main.discipline"))

    disciplines = Discipline.query.all()

    return render_template(
        "pages/discipline/index.html", form=form, disciplines=disciplines
    )


def edit(id):
    discipline = Discipline.query.get_or_404(id)

    form = DisciplineForm(obj=discipline)

    if form.validate_on_submit():
        discipline.name = form.name.data
        discipline.code = form.code.data
        discipline.workload = form.workload.data

        add_data_from_related_tables(form, discipline)

        db.session.commit()

        flash(f"Disipline {discipline.name} updated successfully!", "success")

        return redirect(url_for("main.discipline"))

    form.populate_obj(discipline)

    form.teacher.data = [teacher.id for teacher in discipline.teachers]
    form.course.data = [course.id for course in discipline.courses]

    return render_template(
        "pages/discipline/edit.html", form=form, discipline=discipline
    )


def destroy(id):
    discipline = Discipline.query.get_or_404(id)
    db.session.delete(discipline)
    db.session.commit()
    flash(f"Discipline {discipline.name} deleted successfully!", "success")
    return redirect(url_for("main.discipline"))


def add_data_from_related_tables(form, discipline):
    """
    Add or remove the teachers and courses selected in the form to/from the discipline in the database

    :param form: The form containing the selected teachers and courses
    :param discipline: The discipline to add or remove the teachers and courses to/from
    :return: None
    """

    # Clear existing relationships
    TeacherDiscipline.query.filter_by(discipline_id=discipline.id).delete()
    DisciplineCourse.query.filter_by(discipline_id=discipline.id).delete()

    # Add new relationships based on form data
    for teacherId, courseId in zip_longest(
        form.teacher.data, form.course.data, fillvalue=0
    ):
        if teacherId != 0:
            db.session.add(
                TeacherDiscipline(teacher_id=teacherId, discipline_id=discipline.id)
            )

        if courseId != 0:
            db.session.add(
                DisciplineCourse(discipline_id=discipline.id, course_id=courseId)
            )
