from app import db


class TeacherCourse(db.Model):
    __tablename__ = "teacher_course"

    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), primary_key=True)
