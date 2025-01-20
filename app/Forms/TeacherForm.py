from flask_wtf import FlaskForm
from wtforms import StringField, DateField, RadioField, SelectMultipleField, SubmitField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import DataRequired, Length, Email
from app.Models.Discipline import Discipline
from app.Models.Course import Course


class TeacherForm(FlaskForm):
    name = StringField(
        "Enter your name",
        validators=[
            DataRequired(message="Please enter a name"),
            Length(min=1, max=50, message="Name must be between 1 and 50 characters"),
        ],
    )
    registration = StringField(
        "Enter your registration",
        validators=[
            DataRequired(message="Please enter a registration number"),
            Length(
                min=1,
                max=50,
                message="Registration must be between 1 and 50 characters",
            ),
        ],
    )
    dateOfBirth = DateField(
        "Enter your date of birth",
        format="%Y-%m-%d",
        validators=[
            DataRequired(message="Please enter a date of birth"),
        ],
    )
    gender = RadioField(
        "Enter your gender",
        default=1,
        coerce=int,
        validators=[DataRequired(message="Please enter a gender")],
        choices=[(1, "Male"), (2, "Female")],
    )
    address = StringField(
        "Enter your address",
        validators=[
            DataRequired(message="Please enter an address"),
            Length(
                min=1, max=100, message="Address must be between 1 and 100 characters"
            ),
        ],
    )
    phone = StringField(
        "Enter your phone",
        validators=[
            DataRequired(message="Please enter a phone"),
            Length(min=1, max=50, message="Phone must be between 1 and 50 characters"),
        ],
    )
    email = StringField(
        "Enter your email",
        validators=[
            DataRequired(message="Please enter an email"),
            Email(message="Invalid email address"),
        ],
    )
    discipline = SelectMultipleField(
        "Choose a discipline",
        default=None,
        coerce=int,
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput(),
    )
    course = SelectMultipleField(
        "Choose a course",
        default=None,
        coerce=int,
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput(),
    )
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        self.discipline.choices = [
            (discipline.id, discipline.name) for discipline in Discipline.query.all()
        ]
        self.discipline.choices.insert(0, (0, "No discipline"))
        self.course.choices = [
            (course.id, course.name) for course in Course.query.all()
        ]
        self.course.choices.insert(0, (0, "No course"))
