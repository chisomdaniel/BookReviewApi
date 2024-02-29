#!/usr/bin/env python3
'''the books table'''
from . import db
from datetime import datetime
from models.base import BaseModel


book_genre = db.Table('book_genre',
                      db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
                      db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
                      )


class Book(db.Model, BaseModel):
    '''the book class'''

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    author = db.Column(db.String(100), nullable=False)
    edition = db.Column(db.String(50), nullable=True)
    image = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # handling relationships
    reviews = db.relationship('Review', backref='book', lazy=True)
    genre = db.relationship('Genre', secondary=book_genre, backref='books')

