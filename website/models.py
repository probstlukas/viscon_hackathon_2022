from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import timedelta, datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    endDate = db.Column(db.DateTime(timezone=True), default=datetime.now()+timedelta(hours=3))
    location = db.Column(db.String(10000))
    foods = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    visibility = db.Column(db.Boolean, default=True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    events = db.relationship('Event')