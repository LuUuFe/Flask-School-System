from flask import render_template, redirect, url_for, flash
from app import db
from app.Models.Discipline import Discipline
from app.Models.TeacherDiscipline import TeacherDiscipline
from app.Models.DisciplineCourse import DisciplineCourse
from app.Forms.DisciplineForm import DisciplineForm
from itertools import zip_longest


def index():
    """
    Show all disciplines in the database.
    """

    # Gets all disciplines in the database
    disciplines = Discipline.query.all()

    # Renders the template with the data
    return render_template("pages/discipline/index.html", disciplines=disciplines)


def create():
    """
    Handles the discipline registration form and adds a new discipline to the database.

    If the form is valid, it creates a new Discipline object and adds it to the database.
    After successful registration, it flashes a success message and redirects to the discipline page.

    Otherwise, it renders the form template for discipline creation.
    """

    # Create an instance of the discipline form
    form = DisciplineForm()

    # Check if the form is submitted and valid
    if form.validate_on_submit():
        # Create a new Discipline object with form data
        newDiscipline = Discipline(
            name=form.name.data, code=form.code.data, workload=form.workload.data
        )

        # Add the new discipline to the database session
        db.session.add(newDiscipline)

        # Flush the session to generate any new IDs
        db.session.flush()

        # Add related data from form to the discipline
        add_data_from_related_tables(form, newDiscipline)

        # Commit the changes to the database
        db.session.commit()

        # Flash a success message
        flash("Discipline registered successfully!", "success")

        # Redirect to the discipline page
        return redirect(url_for("main.discipline"))

    # Render the discipline form template
    return render_template("pages/discipline/create.html", form=form)


def edit(id: int):
    """
    Handles the discipline edit form and updates a discipline in the database.

    If the form is valid, it updates the discipline object and commits the changes to the database.
    After successful update, it flashes a success message and redirects to the discipline list page.

    Otherwise, it renders the discipline edit template with the form and discipline data.
    """
    discipline = Discipline.query.get_or_404(id)

    form = DisciplineForm(obj=discipline)

    if form.validate_on_submit():
        # Update the discipline object with the form data
        discipline.name = form.name.data
        discipline.code = form.code.data
        discipline.workload = form.workload.data

        # Add or remove the teachers and courses selected in the form to/from the discipline in the database
        add_data_from_related_tables(form, discipline)

        # Commit the changes to the database
        db.session.commit()

        # Flash a success message
        flash(f"Discipline {discipline.name} updated successfully!", "success")

        # Redirect to the discipline list page
        return redirect(url_for("main.discipline"))

    # Populate the teacher and course select fields with the discipline's data
    form.teacher.data = [teacher.id for teacher in discipline.teachers]
    form.course.data = [course.id for course in discipline.courses]

    # Render the edit template with the form and discipline data
    return render_template(
        "pages/discipline/edit.html", form=form, discipline=discipline
    )


def destroy(id: int):
    """
    Delete a discipline from the database.

    Retrieves the discipline object from the database or returns a 404 error if not found.
    Removes the teachers and courses associated with the discipline from the database.
    Deletes the discipline object from the database and commits the changes.
    Flashes a success message with the discipline's name and redirects to the discipline list page.

    :param id: The ID of the discipline to delete
    :return: A redirect to the discipline list page
    """

    discipline = Discipline.query.get_or_404(id)

    # Remove the teachers and courses associated with the discipline from the database
    remove_data_from_related_tables(discipline)

    # Delete the discipline object from the database and commit the changes
    db.session.delete(discipline)
    db.session.commit()

    # Flash a success message with the discipline's name and redirect to the discipline list page
    flash(f"Discipline {discipline.name} deleted successfully!", "success")
    return redirect(url_for("main.discipline"))


def add_data_from_related_tables(form: DisciplineForm, discipline: Discipline):
    """
    Add or remove the teachers and courses selected in the form to/from the discipline in the database

    :param form: The form containing the selected teachers and courses
    :param discipline: The discipline to add or remove the teachers and courses to/from
    :return: None
    """

    # Clear existing relationships
    remove_data_from_related_tables(discipline)

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


def remove_data_from_related_tables(discipline: Discipline):
    """
    Remove the teachers and courses associated with a discipline from the database

    :param discipline: The discipline to remove the teachers and courses from
    :return: None
    """

    # Clear existing relationships
    TeacherDiscipline.query.filter_by(discipline_id=discipline.id).delete()
    DisciplineCourse.query.filter_by(discipline_id=discipline.id).delete()
