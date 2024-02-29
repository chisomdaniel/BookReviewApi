#!/usr/bin/env python3
'''Flask app file'''
from flask import Flask
from api import api
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import os


load_dotenv()

KEY = os.getenv('APP_KEY')
DATABASE_URI= os.getenv('SQLALCHEMY_DATABASE_URI')
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SECRET_KEY'] = KEY
app.config['JWT_SECRET_KEY'] = KEY

api.init_app(app)
db.init_app(app)
jwt = JWTManager(app)


admin = Admin(app)

with app.app_context():
    from models.books import Book
    from models.reviews import Review
    from models.genres import Genre
    from models.users import User

    admin.add_view(ModelView(Book, db.session))
    admin.add_view(ModelView(Review, db.session))
    admin.add_view(ModelView(Genre, db.session))
    admin.add_view(ModelView(User, db.session))

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()

    #db.drop_all()
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

