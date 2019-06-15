from datetime import datetime
from river_prediction_app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class RiverLevel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    river_name = db.Column(db.String(100))
    station_id = db.Column(db.String(100))
    station_name = db.Column(db.String(100))
    level = db.Column(db.String(100))
    time = db.Column(db.String(100))
    prediction = db.Column(db.String(100))

    def __repr__(self):
        return f"RiverLevel('{self.river_name}', '{self.station_name}', '{self.level}')"


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))
    reason = db.Column(db.String(100))

    def __repr__(self):
        return f"Subscription('{self.name}', '{self.email}', '{self.location}', '{self.reason}')"
