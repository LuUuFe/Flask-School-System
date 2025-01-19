from app import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    registration = db.Column(db.String(50), unique=True, nullable=False)
    date_of_birth = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
