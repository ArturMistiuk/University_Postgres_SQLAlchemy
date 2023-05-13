from datetime import datetime
from random import randint, choice

from faker import Faker

from db_connection import session
from models import Professor, Student, Group, Subject, Mark

fake_data = Faker()

NUMBER_OF_PROFESSORS = 3
NUMBER_OF_STUDENTS = 30
NUMBER_OF_GROUPS = 3
NUMBER_OF_SUBJECTS = 5
NUMBER_OF_MARKS = 150

date_start = datetime.strptime("2022-01-01", "%Y-%m-%d")
date_end = datetime.strptime("2022-12-31", "%Y-%m-%d")
random_date = [
    fake_data.date_between_dates(date_start=date_start, date_end=date_end)
    for _ in range(10)
]


def generate_fake_data():
    for _ in range(NUMBER_OF_PROFESSORS):
        fake_professor = Professor(name=fake_data.name(), email=fake_data.email())
        session.add(fake_professor)

    session.commit()

    for _ in range(NUMBER_OF_STUDENTS):
        fake_student = Student(name=fake_data.name())
        session.add(fake_student)

    session.commit()

    for _ in range(NUMBER_OF_GROUPS):
        fake_group = Group(name=fake_data.job())
        session.add(fake_group)

    session.commit()

    for _ in range(NUMBER_OF_SUBJECTS):
        fake_subject = Subject(name=fake_data.job())
        session.add(fake_subject)

    session.commit()

    for _ in range(NUMBER_OF_MARKS):
        fake_mark = Mark(mark=randint(1, 100), date=choice(random_date))
        session.add(fake_mark)

    session.commit()


if __name__ == '__main__':
    generate_fake_data()
