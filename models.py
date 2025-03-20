from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    topic = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.Integer, default=1)  # 1-5 scale
    tags = db.Column(db.String(200))  # Comma-separated tags
    examples = db.Column(db.Text)
    resources = db.Column(db.Text)  # URLs to additional resources
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class StudySession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, default=1)  # We'll add user system later
    topic = db.Column(db.String(50), nullable=False)
    mode = db.Column(db.String(20), default='standard')  # standard, spaced, quiz
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    cards_studied = db.Column(db.Integer, default=0)
    correct_answers = db.Column(db.Integer, default=0)

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, default=1)
    topic = db.Column(db.String(50), nullable=False)
    cards_reviewed = db.Column(db.Integer, default=0)
    correct_answers = db.Column(db.Integer, default=0)
    study_time = db.Column(db.Integer, default=0)  # in minutes
    last_studied = db.Column(db.DateTime, default=datetime.utcnow) 