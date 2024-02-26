#!/usr/bin/env python3
'''categorize the tables into different genres'''
from . import db
from datetime import datetime
from models.base import BaseModel


class Genre(db.Model, BaseModel):
    '''the genre class'''

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

