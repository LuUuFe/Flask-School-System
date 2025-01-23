from flask_wtf import FlaskForm
from wtforms import StringField, DateField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from app.Models.Course import Course


class StudentForm(FlaskForm):
    name = StringField(
        "Enter your name",
        validators=[
            DataRequired(message="Please enter a name"),
            Length(min=1, max=50, message="Name must be between 1 and 50 characters"),
        ],
    )
    registration = StringField(
        "Enter your registration",
        validators=[DataRequired(message="Please enter a registration number")],
    )
    dateOfBirth = DateField(
        "Enter your date of birth",
        validators=[DataRequired(message="Please enter a date of birth")],
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
            DataRequired(message="Please enter a phone number"),
            Length(
                min=10, max=15, message="Phone number must be between 10 and 15 digits"
            ),
        ],
    )
    email = StringField(
        "Enter your email",
        validators=[
            DataRequired(message="Please enter an email"),
            Email(message="Invalid email address"),
        ],
    )
    course = SelectField("Choose a course", default=None, coerce=int)
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.course.choices = [
            (course.id, course.name) for course in Course.query.all()
        ]
        self.course.choices.insert(0, (0, "No course"))
