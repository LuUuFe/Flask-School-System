from app import db


class TeacherDiscipline(db.Model):
    __tablename__ = "teacher_discipline"

    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"), primary_key=True)
    discipline_id = db.Column(
        db.Integer, db.ForeignKey("disciplines.id"), primary_key=True
    )
