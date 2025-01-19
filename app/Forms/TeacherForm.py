from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectMultipleField, SubmitField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import DataRequired
from app.Models.Discipline import Discipline
from app.Models.Course import Course


class TeacherForm(FlaskForm):
    name = StringField("Enter your name", validators=[DataRequired()])
    registration = StringField("Enter your registration", validators=[DataRequired()])
    dateOfBirth = DateField(
        "Enter your date of birth", format="%Y-%m-%d", validators=[DataRequired()]
    )
    gender = StringField("Enter your gender", validators=[DataRequired()])
    address = StringField("Enter your address", validators=[DataRequired()])
    phone = StringField("Enter your phone", validators=[DataRequired()])
    email = StringField("Enter your email", validators=[DataRequired()])
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
