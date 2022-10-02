from sqlalchemy import String, Integer, Column, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship

from .connection import Base, session, engine


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    students = relationship("Student", back_populates="teacher")

    def __str__(self):
        return f'{self.surname.title()} {self.name.title()}'

    @classmethod
    def add(cls, name, surname):
        teacher = cls(name=name, surname=surname)
        session.add(teacher)
        session.commit()
        return teacher

    @classmethod
    def all(cls):
        return session.query(cls).all()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(SmallInteger)
    phone = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher", back_populates="students")

    @classmethod
    def add(cls, name, age, phone, teacher, surname):
        student = cls(name=name, age=age, phone=phone, teacher=teacher, surname=surname)
        session.add(student)
        session.commit()
        return student


Base.metadata.create_all(engine)
