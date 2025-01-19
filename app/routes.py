from flask import Blueprint, render_template
from app.Controllers import (
    StudentController,
    TeacherController,
    DisciplineController,
    CourseController,
)

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    return render_template("nav.html")


@main.route("/students", methods=["GET", "POST"])
def student():
    return StudentController.index()


@main.route("/student/edit/<int:id>", methods=["GET", "POST"])
def student_edit(id):
    return StudentController.edit(id)


@main.route("/student/destroy/<int:id>", methods=["GET", "POST"])
def student_destroy(id):
    return StudentController.destroy(id)


@main.route("/teachers", methods=["GET", "POST"])
def teacher():
    return TeacherController.teacher()
  
@main.route("/teacher/edit/<int:id>", methods=["GET", "POST"])
def teacher_edit(id):
    return TeacherController.edit(id)


@main.route("/teacher/destroy/<int:id>", methods=["GET", "POST"])
def teacher_destroy(id):
    return TeacherController.destroy(id)


@main.route("/discipline", methods=["GET", "POST"])
def discipline():
    return DisciplineController.discipline()


@main.route("/course", methods=["GET", "POST"])
def course():
    return CourseController.course()
