from app import db


class Discipline(db.Model):
    __tablename__ = "disciplines"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)
    workload = db.Column(db.String(20), nullable=False)

    teachers = db.relationship(
        "Teacher", secondary="teacher_discipline", back_populates="disciplines"
    )
    courses = db.relationship(
        "Course", secondary="discipline_course", back_populates="disciplines"
    )
