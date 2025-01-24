from flask import render_template, flash, redirect, url_for
from app import db
from app.Models.Student import Student
from app.Models.TeacherCourse import TeacherCourse
from app.Models.DisciplineCourse import DisciplineCourse
from app.Models.Course import Course
from app.Forms.CourseForm import CourseForm
from itertools import zip_longest


def index():
    """
    Display all courses available in the database.

    :return: A rendered template with all courses
    """

    # Retrieve all courses from the database
    courses = Course.query.all()

    # Render the course index template with the list of courses
    return render_template("pages/course/index.html", courses=courses)


def create():
    """
    Handles the course creation form and adds a new course to the database.

    If the form is valid, it creates a new Course object and adds it to the database.
    After successful creation, it flashes a success message and redirects to the course page.

    Otherwise, it renders the create.html template with the course form.
    """

    # Create an instance of the course form
    form = CourseForm()

    # Check if the form is submitted and valid
    if form.validate_on_submit():
        # Extract data from the form
        name = form.name.data
        code = form.code.data

        # Create a new Course object with form data
        newCourse = Course(name=name, code=code)

        # Add the new course to the database session
        db.session.add(newCourse)

        # Flush the session to generate any new IDs
        db.session.flush()

        # Add related data from form to the course
        add_data_from_related_tables(form, newCourse)

        # Commit the changes to the database
        db.session.commit()

        # Flash a success message
        flash("Course registered successfully!", "success")

        # Redirect to the course page
        return redirect(url_for("main.course"))

    # Render the course form template
    return render_template("pages/course/create.html", form=form)


def edit(id: int):
    """
    Handles the course edit form and updates a course in the database.

    If the form is valid, it updates the course object and commits the changes to the database.
    After successful update, it flashes a success message and redirects to the course page.

    Otherwise, it renders the edit.html template with the course form and course data.
    """

    course = Course.query.get_or_404(id)

    # Create an instance of the course form with the course object
    form = CourseForm(obj=course)

    # Check if the form is submitted and valid
    if form.validate_on_submit():
        # Update the course object with the form data
        course.name = form.name.data
        course.code = form.code.data

        # Add or remove related data from the form to the course
        add_data_from_related_tables(form, course)

        # Commit the changes to the database
        db.session.commit()

        # Flash a success message
        flash(f"Course {course.name} updated successfully!", "success")

        # Redirect to the course page
        return redirect(url_for("main.course"))

    # Populate the student, teacher, and discipline select fields with the course's data
    form.student.data = [student.id for student in course.students]
    form.teacher.data = [teacher.id for teacher in course.teachers]
    form.discipline.data = [discipline.id for discipline in course.disciplines]

    # Render the edit template with the form and course data
    return render_template("pages/course/edit.html", form=form, course=course)


def destroy(id: int):
    """
    Deletes a course from the database.

    Retrieves the course object from the database or returns a 404 error if not found.
    Removes the relationships of the course with students, teachers, and disciplines from the database.
    Deletes the course object from the database and commits the changes.
    Flashes a success message with the course's name and redirects to the course list page.

    :param id: The ID of the course to delete
    :return: A redirect to the course list page
    """

    # Retrieve the course object from the database or return a 404 error if not found
    course = Course.query.get_or_404(id)

    # Remove the relationships of the course with students, teachers, and disciplines from the database
    remove_data_from_related_tables(course)

    # Delete the course object from the database and commit the changes
    db.session.delete(course)
    db.session.commit()

    # Flash a success message with the course's name and redirect to the course list page
    flash(f"Course {course.name} deleted successfully!", "success")
    return redirect(url_for("main.course"))


def add_data_from_related_tables(form: CourseForm, course: Course):
    """
    Update the relationships of a course with students, teachers, and disciplines
    based on the provided form data. Existing relationships are cleared before
    adding the new ones.

    :param form: The form containing the new student, teacher, and discipline data.
    :param course: The course whose relationships need to be updated.
    :return: None
    """

    # Clear existing relationships
    remove_data_from_related_tables(course)

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


def remove_data_from_related_tables(course: Course):
    """
    Remove the relationships of a course with students, teachers, and disciplines
    from the database.

    :param course: The course whose relationships need to be removed.
    :return: None
    """

    # Clear existing relationships
    Student.query.filter_by(course_id=course.id).delete()
    TeacherCourse.query.filter_by(course_id=course.id).delete()
    DisciplineCourse.query.filter_by(course_id=course.id).delete()
