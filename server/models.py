from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData, Column, Integer, ForeignKey, Table
from sqlalchemy.orm import validates, relationship
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from config import db, bcrypt

# Models go here!

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    role = db.Column(db.String)
    username = db.Column(db.String, nullable = False, unique = True)
    email = db.Column(db.String)
    _password_hash = db.Column(db.String, nullable=False)
    approved_user = db.Column(db.Boolean, default=False, index=True)

    #role = parent, student, professional and then provided the appropriate site access
    # emotions = db.relationship('Emotion', back_populates='user')

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        # utf-8 encoding and decoding is required in python 3
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))
    
    def __repr__(self):
        return f"<User {self.username}>"
    
    @validates("email")
    def validate_email(self, key, email):
        if "@" not in email:
            raise ValueError("Email invalid")
        if len(email) > 40:
            raise ValueError(
                "Email must be less than 40 characters long"
            )
        return email
    
class Emotion(db.Model):
    __tablename__ = 'emotions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    count = db.Column(db.Integer)
    total = db.Column(db.Integer)
    resource = db.Column(db.String)

    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # user = db.relationship('User', back_populates='emotions')

    # def __repr__(self):
    #     return f'<Emotion {self.id}>'

class Goal(db.Model):
    __tablename__ = 'goals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    activity = db.Column(db.String)
    resource = db.Column(db.String)

    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # user = db.relationship('User', back_populates='goals')

    # evaluation_id = db.Column(db.Integer, db.ForeignKey('evaluations.id'))
    # evaluation = db.relationship('Evaluation', back_populates='evaluations')

    # serialize_rules=('-evaluations_relationship',)
    # def __repr__(self):
    #     return f'<Goal {self.id}>'

class Evaluation(db.Model):
    __tablename__ = 'evaluations'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    question_id = db.Column(db.integer,db.ForeignKey("questions.id"))
    response_id = db.Column(db.integer,db.ForeignKey("responses.id"))

    # questions_relationship = db.relationship('Question', back_populates='responses_relationship', cascade="all,delete")
    # responses_relationship = db.relationship('Response', back_populates='questions_relationship', cascade="all,delete")

    # user = db.relationship('User', back_populates='evaluations_relationship', cascade="all,delete")

    #serialize_rules = ('-questions_relationship', '-responses_relationship',)
    # def __repr__(self):
    #     return f'<Evaluation {self.id}>'

class Question(db.Model):
    __tablename__= 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    options = db.Column(db.String)

    # user = db.relationship('User', back_populates='questions_relationship', cascade="all,delete")

    #serialize_rules = ('-responses_relationship',)
    # def __repr__(self):
    #     return f'<Question {self.id}>'

class Response(db.Model):
    __tablename__= 'responses'

    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String)
    answers = db.Column(db.String)
    comments = db.Column(db.String)

    # user = db.relationship('User', back_populates='responses_relationship', cascade="all,delete")

    #serialize_rules = ('-questions_relationship',)
    # def __repr__(self):
    #     return f'<Response {self.id}>'