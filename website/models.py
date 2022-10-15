from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import timedelta, datetime


'''class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    endDate = db.Column(db.DateTime(timezone=True), default=datetime.now()+timedelta(hours=3))
    location = db.Column(db.String(1000))
    foods = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    visibility = db.Column(db.Boolean, default=True)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    events = db.relationship('Event')

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ending = db.Column(db.String(100))


'''
######### NEW NEW NEW NEW



class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    user = db.Column(db.Integer)
    location = db.Column(db.String(200))
    creationDate = db.Column(db.DateTime(timezone=True), default=func.now())
    expirationDate = db.Column(db.DateTime(timezone=True), default=datetime.now()+timedelta(hours=3))
    visibility = db.Column(db.Boolean, default=True)
    imageId = db.Column(db.Integer)

class Foods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suffix = db.Column(db.String(10))

class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(150))
    email = db.Column(db.String(100))
    name = db.Column(db.String(100))

class Ehfht(db.Model):
    eventsId = db.Column(db.Integer, primary_key=True)
    tagsId = db.Column(db.Integer, primary_key=True)
    foodsId = db.Column(db.Integer, primary_key=True)
    portions = db.Column(db.Integer)
    interest = db.Column(db.Integer)