from flask import Blueprint, render_template
from app.Controllers import (
    StudentController,
    TeacherController,
    DisciplineController,
    CourseController,
)

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def index():
    return render_template("nav.html")


@main.route("/students", methods=["GET"])
def student():
    return StudentController.index()


@main.route("/student/create", methods=["GET", "POST"])
def student_create():
    return StudentController.create()


@main.route("/student/edit/<int:id>", methods=["GET", "POST"])
def student_edit(id: int):
    return StudentController.edit(id)


@main.route("/student/destroy/<int:id>", methods=["GET", "POST"])
def student_destroy(id: int):
    return StudentController.destroy(id)


@main.route("/teachers", methods=["GET"])
def teacher():
    return TeacherController.index()


@main.route("/teacher/create", methods=["GET", "POST"])
def teacher_create():
    return TeacherController.create()


@main.route("/teacher/edit/<int:id>", methods=["GET", "POST"])
def teacher_edit(id: int):
    return TeacherController.edit(id)


@main.route("/teacher/destroy/<int:id>", methods=["GET", "POST"])
def teacher_destroy(id):
    return TeacherController.destroy(id)


@main.route("/disciplines", methods=["GET"])
def discipline():
    return DisciplineController.index()


@main.route("/discipline/create", methods=["GET", "POST"])
def discipline_create():
    return DisciplineController.create()


@main.route("/discipline/edit/<int:id>", methods=["GET", "POST"])
def discipline_edit(id: int):
    return DisciplineController.edit(id)


@main.route("/discipline/destroy/<int:id>", methods=["GET", "POST"])
def discipline_destroy(id: int):
    return DisciplineController.destroy(id)


@main.route("/courses", methods=["GET", "POST"])
def course():
    return CourseController.index()


@main.route("/course/edit/<int:id>", methods=["GET", "POST"])
def course_edit(id):
    return CourseController.edit(id)


@main.route("/course/destroy/<int:id>", methods=["GET", "POST"])
def course_destroy(id):
    return CourseController.destroy(id)
