from app import db

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
  
  disciplines = db.relationship('Discipline', backref='teacher', lazy=True)

class Discipline(db.Model):
  __tablename__ = 'disciplines'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  code = db.Column(db.String(50), unique=True, nullable=False)
  workload = db.Column(db.String(20), nullable=False)
  
  teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
  
  classes = db.relationship('Class', backref='discipline', lazy=True)

class Class(db.Model):
  __tablename__ = 'classes'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  code = db.Column(db.String(50), unique=True, nullable=False)
  
  discipline_id = db.Column(db.Integer, db.ForeignKey('disciplines.id'), nullable=False)
  
  teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
  