from app import db


class DisciplineCourse(db.Model):
    __tablename__ = "discipline_course"

    discipline_id = db.Column(
        db.Integer, db.ForeignKey("disciplines.id"), primary_key=True
    )
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), primary_key=True)
