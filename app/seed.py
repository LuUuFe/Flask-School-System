from app import db
from app.models import (
    Student,
    Teacher,
    Discipline,
    Course,
    TeacherDiscipline,
    TeacherCourse,
    DisciplineCourse,
)
from faker import Faker
import random

faker = Faker()


def seed_data():
    # Limpando os dados existentes no banco de dados
    db.drop_all()
    db.create_all()

    # Criando Cursos
    courses = []
    for _ in range(5):  # Cria 5 cursos de exemplo
        course = Course(
            name=faker.unique.job(),
            code=f"CRS{faker.unique.random_int(min=100, max=999)}",
        )
        courses.append(course)
    db.session.add_all(courses)
    db.session.commit()

    # Criando Disciplinas
    disciplines = []
    for _ in range(10):  # Cria 10 disciplinas de exemplo
        discipline = Discipline(
            name=faker.unique.bs().title(),
            code=f"DSC{faker.unique.random_int(min=100, max=999)}",
            workload=f"{random.choice([30, 45, 60, 90])}h",
        )
        disciplines.append(discipline)
    db.session.add_all(disciplines)
    db.session.commit()

    # Relacionando disciplinas a cursos
    for course in courses:
        assigned_disciplines = faker.random_elements(
            elements=disciplines, length=random.randint(2, 5), unique=True
        )
        course.disciplines.extend(assigned_disciplines)
    db.session.commit()

    # Criando Professores
    teachers = []
    for _ in range(10):  # Cria 10 professores de exemplo
        teacher = Teacher(
            name=faker.name(),
            registration=f"T{faker.unique.random_int(min=1000, max=9999)}",
            date_of_birth=faker.date_of_birth(minimum_age=25, maximum_age=60).strftime(
                "%Y-%m-%d"
            ),
            gender=random.choice(["Male", "Female"]),
            address=faker.address(),
            phone=faker.phone_number(),
            email=faker.unique.email(),
        )
        teachers.append(teacher)
    db.session.add_all(teachers)
    db.session.commit()

    # Relacionando professores a disciplinas e cursos
    for teacher in teachers:
        assigned_disciplines = faker.random_elements(
            elements=disciplines, length=random.randint(1, 3), unique=True
        )
        assigned_courses = faker.random_elements(
            elements=courses, length=random.randint(1, 2), unique=True
        )
        teacher.disciplines.extend(assigned_disciplines)
        teacher.courses.extend(assigned_courses)
    db.session.commit()

    # Criando Estudantes
    students = []
    for _ in range(50):  # Cria 50 estudantes de exemplo
        student = Student(
            name=faker.name(),
            registration=f"S{faker.unique.random_int(min=1000, max=9999)}",
            date_of_birth=faker.date_of_birth(minimum_age=18, maximum_age=25).strftime(
                "%Y-%m-%d"
            ),
            gender=random.choice(["Male", "Female"]),
            address=faker.address(),
            phone=faker.phone_number(),
            email=faker.unique.email(),
            course_id=random.choice(courses).id,
        )
        students.append(student)
    db.session.add_all(students)
    db.session.commit()

    print("Dados inicializados com sucesso!")
