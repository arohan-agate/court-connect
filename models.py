from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150), nullable=True)
    phone = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(150), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    sports = db.Column(db.String(200), nullable=True)
    interests = db.Column(db.String(200), nullable=True)
    location_city = db.Column(db.String(100), nullable=True)
    location_state = db.Column(db.String(50), nullable=True)
    languages = db.Column(db.String(200), nullable=True)
    gender = db.Column(db.String(50), nullable=True)
    pronouns = db.Column(db.String(50), nullable=True)
    school_work = db.Column(db.String(150), nullable=True)
    profile_picture = db.Column(db.String(250), nullable=True)  # To store image file path

    def __repr__(self):
        return f'<User {self.username}>'
