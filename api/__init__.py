#!/usr/bin/env python3
'''set up our api'''
from flask_restful import Api
from api.status import Status
from api.book_api import BooksResource
from api.review_api import ReviewsResource
from api.user_api import Login, Signup, User, Users
#from app import app

api = Api()


api.add_resource(Status, '/status', strict_slashes=False)
api.add_resource(BooksResource, '/api/book/', '/api/book/<int:id>', strict_slashes=False)
api.add_resource(ReviewsResource, '/api/book/<int:book_id>/review', '/api/book/<int:book_id>/review/<int:review_id>', strict_slashes=False)
api.add_resource(Login, '/api/login', strict_slashes=False)
api.add_resource(Signup, '/api/signup', strict_slashes=False)
api.add_resource(User, '/api/me', strict_slashes=False)
api.add_resource(Users, '/api/users', strict_slashes=False)

