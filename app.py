#!/usr/bin/env python3
'''Flask app file'''
from flask import Flask
from api import api
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager


load_dotenv()

key = '23578g29h293r8h29402490'
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://daniel:ezewnihc@localhost/book_log'
app.config['SECRET_KEY'] = key
app.config['JWT_SECRET_KEY'] = key

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
    admin.add_view(ModelView(User, db.seesion))

    @jwt.user_lookup_loder
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()

    #db.drop_all()
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

