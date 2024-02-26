#!/usr/bin/env python3
'''the review and rating table'''
from . import db
from datetime import datetime
from models.base import BaseModel


class Review(db.Model, BaseModel):
    '''the review class'''

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


