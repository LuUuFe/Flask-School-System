from app import db
from app.models import Student, Teacher, Discipline, Course, TeacherDiscipline, TeacherCourse, DisciplineCourse

def seed_data():
    # Limpando os dados existentes no banco de dados
    db.drop_all()
    db.create_all()

    # Criando Cursos
    course1 = Course(name="Computer Science", code="CS101")
    course2 = Course(name="Mechanical Engineering", code="ME102")
    db.session.add_all([course1, course2])
    db.session.commit()

    # Criando Disciplinas
    discipline1 = Discipline(name="Data Structures", code="CS201", workload="60h")
    discipline2 = Discipline(name="Thermodynamics", code="ME202", workload="45h")
    db.session.add_all([discipline1, discipline2])
    db.session.commit()

    # Relacionando disciplinas a cursos
    course1.disciplines.append(discipline1)
    course2.disciplines.append(discipline2)
    db.session.commit()

    # Criando Professores
    teacher1 = Teacher(
        name="Alice Johnson",
        registration="T1001",
        date_of_birth="1980-05-15",
        gender="Female",
        address="123 Main Street",
        phone="1234567890",
        email="alice.johnson@example.com"
    )
    teacher2 = Teacher(
        name="Bob Smith",
        registration="T1002",
        date_of_birth="1975-09-22",
        gender="Male",
        address="456 Oak Avenue",
        phone="0987654321",
        email="bob.smith@example.com"
    )
    db.session.add_all([teacher1, teacher2])
    db.session.commit()

    # Relacionando professores a disciplinas e cursos
    teacher1.disciplines.append(discipline1)
    teacher2.disciplines.append(discipline2)
    teacher1.courses.append(course1)
    teacher2.courses.append(course2)
    db.session.commit()

    # Criando Estudantes
    student1 = Student(
        name="Charlie Brown",
        registration="S2001",
        date_of_birth="2001-03-12",
        gender="Male",
        address="789 Elm Street",
        phone="1122334455",
        email="charlie.brown@example.com",
        course_id=course1.id
    )
    student2 = Student(
        name="Diana Prince",
        registration="S2002",
        date_of_birth="2000-07-19",
        gender="Female",
        address="321 Pine Road",
        phone="5566778899",
        email="diana.prince@example.com",
        course_id=course2.id
    )
    db.session.add_all([student1, student2])
    db.session.commit()

    print("Dados inicializados com sucesso!")
