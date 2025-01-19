from app import db


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)

    students = db.relationship("Student", backref="course", lazy=True)

    teachers = db.relationship(
        "Teacher", secondary="teacher_course", back_populates="courses"
    )
    disciplines = db.relationship(
        "Discipline", secondary="discipline_course", back_populates="courses"
    )
