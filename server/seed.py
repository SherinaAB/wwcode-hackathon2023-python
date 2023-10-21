from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Emotion, Goal, Evaluation, Question, Response

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
            role = fake.role(),
            username = fake.user_name(),
            email = fake.email(),
            password_hash = "123abc", 
        )
        users.append(u)
    return users

# def create_emotions():
#     emotions = []
#     for _ in range(50):
#         emotions.append(
#             Emotion(
#                 name = fake.text(max_nb_chars = 20),
#             )
#         )
#     return emotions

# def create_goals():
#     goals = []
#     for _ in range(50):
#         goals.append(
#             Goal(
#                 name = fake.text(max_nb_chars = 20),
#                 activity = fake.text(max_nb_chars = 20),
#             )
#         )
#     return goals

# def create_evaluations():
#     evaluations = []
#     for _ in range(50):
#         evaluations.append(
#             Evaluation(
#                 title = fake.text(max_nb_chars = 20),
#             )
#         )
#     return evaluations

# def create_questions():
#     questions = []
#     for _ in range(50):
#         questions.append(
#             Question(
#                 text = fake.text(max_nb_chars = 20),
#                 options = fake.text(max_nb_chars = 20),
#             )
#         )
#     return questions

# def create_responses():
#     responses = []
#     for _ in range(50):
#         responses.append(
#             Response(
#                 activity = fake.text(max_nb_chars = 20),
#                 answers = fake.text(max_nb_chars = 20),
#                 comments = fake.text(max_nb_chars = 20),
#             )
#         )
#     return responses

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        
        print("Clearing database...")
        User.query.delete()
        # Emotion.query.delete()
        # Goal.query.delete()
        # Evaluation.query.delete()
        # Question.query.delete()
        # Response.query.delete()

        print("Seeding users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        # print("Seeding emotions...")
        # emotions = [
        #     Emotion(name='Angry'),
        #     Emotion(name='Happy'),
        #     Emotion(name='Sad'),
        #     Emotion(name='Anxious'),
        #     Emotion(name='Other'),
        # ]

        # db.session.add_all(emotions)
        # db.session.commit()

        # print("Seeding goals...")
        # goals = [
        #     Goal(name='Yoga'),
        #     Goal(name='Mediation'),
        #     Goal(name='Color'),
        #     Goal(name='Walk'),
        #     Goal(name='More'),
        # ]
        
        # db.session.add_all(goals)
        # db.session.commit()

        # print("Seeding evaluations...")
        # evaluations = create_evaluations()
        # db.session.add_all(evaluations)
        # db.session.commit()

        print("Done seeding!")