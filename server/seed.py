#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Emotion, Goal

def create_database():
 with app.app_context():
        db.create_all()

def create_users():
    users = []
    for _ in range(50):
        is_approved = fake.boolean(chance_of_getting_true = 50)
        u = User(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            username = fake.user_name(),
            email = fake.email(),
            password_hash = "123abc", 
            approved_user = is_approved,
        )
        users.append(u)
    return users

def create_emotions():
    emotions = []
    for _ in range(50):
        is_approved = fake.boolean(chance_of_getting_true = 50)
        u = User(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            username = fake.user_name(),
            email = fake.email(),
            password_hash = "123abc", 
            approved_user = is_approved,
        )
        users.append(u)
    return users

def create_users():
    users = []
    for _ in range(50):
        is_approved = fake.boolean(chance_of_getting_true = 50)
        u = User(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            username = fake.user_name(),
            email = fake.email(),
            password_hash = "123abc", 
            approved_user = is_approved,
        )
        users.append(u)
    return users

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        print("Clearing database...")
        User.query.delete()
        Emotion.query.delete()
        Goal.query.delete()

        print("Seeding users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        print("Seeding emotions...")
        emotions = create_emotions()
        db.session.add_all(emotions)
        db.session.commit()

        print("Seeding goals...")
        goals = create_goals()
        db.session.add_all(goals)
        db.session.commit()
