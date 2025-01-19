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


@main.route("/student", methods=["GET", "POST"])
def student():
    return StudentController.student()


@main.route("/teacher", methods=["GET", "POST"])
def teacher():
    return TeacherController.teacher()


@main.route("/discipline", methods=["GET", "POST"])
def discipline():
    return DisciplineController.discipline()


@main.route("/course", methods=["GET", "POST"])
def course():
    return CourseController.course()
