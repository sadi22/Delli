__author__ = 'Sadi'
from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    # phonenumber = db.relationship('PhoneNumber')
    addresses = db.relationship('Address' , backref = 'user' , lazy= 'dynamic')

    # this is one to many


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    house = db.Column(db.Integer)
    area = db.Column(db.String)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))


# class PhoneNumber(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     home = db.Column(db.Integer)
#     self = db.Column(db.Integer)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy= 'dynamic')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
