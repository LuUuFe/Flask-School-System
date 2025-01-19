from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired
from app.Models.Course import Course


class StudentForm(FlaskForm):
    name = StringField("Enter your name", validators=[DataRequired()])
    registration = StringField("Enter your registration", validators=[DataRequired()])
    dateOfBirth = DateField(
        "Enter your date of birth", format="%Y-%m-%d", validators=[DataRequired()]
    )
    gender = StringField("Enter your gender", validators=[DataRequired()])
    address = StringField("Enter your address", validators=[DataRequired()])
    phone = StringField("Enter your phone", validators=[DataRequired()])
    email = StringField("Enter your email", validators=[DataRequired()])
    course = SelectField("Choose a course", default=None, coerce=int)
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        """
        Initializes the StudentForm and populates the course choices.

        Retrieves all courses from the database and sets them as choices for
        the course SelectField. Adds a default option "No course" at the
        beginning of the choices list.
        """
        super(StudentForm, self).__init__(*args, **kwargs)
        self.course.choices = [
            (course.id, course.name) for course in Course.query.all()
        ]
        self.course.choices.insert(0, (0, "No course"))
