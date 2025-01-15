from app import db

class TeacherDiscipline(db.Model):
  __tablename__ = 'teacher_discipline'

  teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), primary_key=True)
  discipline_id = db.Column(db.Integer, db.ForeignKey('disciplines.id'), primary_key=True)

class Student(db.Model):
  __tablename__ = 'students'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  registration = db.Column(db.String(50), unique=True, nullable=False)
  date_of_birth = db.Column(db.String(20), nullable=False)
  gender = db.Column(db.String(10), nullable=False)
  address = db.Column(db.String(255), nullable=False)
  phone = db.Column(db.String(15), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)

class Teacher(db.Model):
  __tablename__ = 'teachers'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  registration = db.Column(db.String(50), unique=True, nullable=False)
  date_of_birth = db.Column(db.String(20), nullable=False)
  gender = db.Column(db.String(10), nullable=False)
  address = db.Column(db.String(255), nullable=False)
  phone = db.Column(db.String(15), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)

  disciplines = db.relationship('Discipline', secondary='teacher_discipline', back_populates='teachers')

class Discipline(db.Model):
  __tablename__ = 'disciplines'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  code = db.Column(db.String(50), unique=True, nullable=False)
  workload = db.Column(db.String(20), nullable=False)
  
  teachers = db.relationship('Teacher', secondary='teacher_discipline', back_populates='disciplines')
  
class Course(db.Model):
  __tablename__ = 'courses'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  code = db.Column(db.String(50), unique=True, nullable=False)
  
  discipline_id = db.Column(db.Integer, db.ForeignKey('disciplines.id'), nullable=False)
  
  teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
  