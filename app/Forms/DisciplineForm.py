from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import DataRequired, Length
from app.Models.Teacher import Teacher
from app.Models.Course import Course


class DisciplineForm(FlaskForm):
    name = StringField(
        "Enter a name",
        validators=[
            DataRequired(message="Please enter a name"),
            Length(min=1, max=50, message="Name must be between 1 and 50 characters"),
        ],
    )
    code = StringField(
        "Enter a code",
        validators=[
            DataRequired(message="Please enter a code"),
            Length(min=1, max=50, message="Code must be between 1 and 50 characters"),
        ],
    )
    workload = StringField(
        "Enter a workload",
        validators=[
            DataRequired(message="Please enter a workload"),
            Length(
                min=1, max=50, message="Workload must be between 1 and 50 characters"
            ),
        ],
    )
    teacher = SelectMultipleField(
        "Choose a teacher",
        coerce=int,
        default=None,
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput(),
    )
    course = SelectMultipleField(
        "Choose a course",
        coerce=int,
        default=None,
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput(),
    )
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(DisciplineForm, self).__init__(*args, **kwargs)
        self.teacher.choices = [
            (teacher.id, teacher.name) for teacher in Teacher.query.all()
        ]
        self.teacher.choices.insert(0, (0, "No teacher"))
        self.course.choices = [
            (course.id, course.name) for course in Course.query.all()
        ]
        self.course.choices.insert(0, (0, "No course"))
