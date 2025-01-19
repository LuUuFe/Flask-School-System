from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import DataRequired
from app.Models.Student import Student
from app.Models.Teacher import Teacher
from app.Models.Discipline import Discipline


class CourseForm(FlaskForm):
    name = StringField("Enter a name", validators=[DataRequired()])
    code = StringField("Enter a code", validators=[DataRequired()])
    student = SelectMultipleField(
        "Choose a student",
        default=None,
        coerce=int,
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput(),
    )
    teacher = SelectMultipleField(
        "Choose a teacher",
        default=None,
        coerce=int,
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput(),
    )
    discipline = SelectMultipleField(
        "Choose a discipline",
        default=None,
        coerce=int,
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput(),
    )
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.student.choices = [
            (student.id, student.name) for student in Student.query.all()
        ]
        self.student.choices.insert(0, (0, "No student"))
        self.teacher.choices = [
            (teacher.id, teacher.name) for teacher in Teacher.query.all()
        ]
        self.teacher.choices.insert(0, (0, "No teacher"))
        self.discipline.choices = [
            (discipline.id, discipline.name) for discipline in Discipline.query.all()
        ]
        self.discipline.choices.insert(0, (0, "No discipline"))
