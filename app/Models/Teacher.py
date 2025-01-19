from app import db


class Teacher(db.Model):
    __tablename__ = "teachers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    registration = db.Column(db.String(50), unique=True, nullable=False)
    date_of_birth = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    disciplines = db.relationship(
        "Discipline", secondary="teacher_discipline", back_populates="teachers"
    )
    courses = db.relationship(
        "Course", secondary="teacher_course", back_populates="teachers"
    )
