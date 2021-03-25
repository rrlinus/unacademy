"""
Define the User model
"""

from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, Boolean
from . import db

class User(db.Model):
    """ The User model """

    __tablename__ = "api_token"

    id = Column(db.Integer, primary_key=True)

    token = Column(
        String(150),
        nullable=False
    )

    active = Column(
        Boolean,
        default=True
    )

    root_uid = Column(
        Integer,
        ForeignKey('users.user_id'),
        server_default=db.text('-1'),
        nullable=False
    )


class Courses(db.Model):
    __tablename__ = "course"

    course_id = Column(db.Integer, primary_key=True)

    course_name = Column(
        String(150),
        nullable=False
    )


class Subject(db.Model):
    __tablename__ = "subjects"
    subject_id = Column(db.Integer, primary_key=True)
    subject_name = Column(
        String(150),
        nullable=False
    )


class Syllabus(db.Model):
    __tablename__ = "syllabus"
    id = Column(db.Integer, primary_key=True)
    course_id = Column(
        Integer,
        ForeignKey('courses.course_id'),
        server_default=db.text('-1'),
        nullable=False
    )
    subject_id = Column(
        Integer,
        ForeignKey('courses.course_id'),
        server_default=db.text('-1'),
        nullable=False
    )

class Video(db.Model):
    __tablename__ = 'videos'
    video_id = Column(db.Integer, primary_key=True)
    subject_id= Column(
        Integer,
        ForeignKey('subjects.subject_id'),
        server_default=db.text('-1'),
        nullable=False
    )
    video_url = Column(
        String(150),
        ForeignKey('courses.course_id'),
        server_default=db.text('-1'),
        nullable=False
    )
    # teacher_id = Column(
    #     Integer,
    #     ForeignKey('subjects.subject_id'),
    #     server_default=db.text('-1'),
    #     nullable=False
    # )
class Client(db.Model):
    __tablename__ = 'users'
    id = Column(db.Integer, primary_key=True)
    user_id = Column(db.Integer)
    course_id = Column(
        Integer,
        ForeignKey('courses.course_id'),
        server_default=db.text('-1'),
        nullable=False
    )

