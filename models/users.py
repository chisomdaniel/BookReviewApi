#!/usr/bin/env python3
'''the review and rating table'''
from . import db
from datetime import datetime
from models.base import BaseModel
import bcrypt


class User(db.Model, BaseModel):
    '''the user class'''

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    avater = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    reviews = db.relationship('Review', backref='book', lazy=True)
    books = db.relationship('Book', backref='user', lazy=True)

    @password.setter
    def hash_password(self, password):
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed_pw
    

    def check_pasword(self, password):
        '''Return True or False if the password is correct'''
        check = bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
        return check
