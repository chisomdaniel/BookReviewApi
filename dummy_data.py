#!/usr/bin/env python3
'''Adds some dummy data to our database.
Running this file will delete all existing data in
the data base and add new ones'''
from models import db
from models.books import Book
from models.reviews import Review
from models.genres import Genre
from models.users import User
from app import app


with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username='Dannyboy', firstname='Daniel', lastname='Chinweze', email='dannyboy@gmail.com', gender='Male', avater='img-dog_paint.png')
    user2 = User(username='Chisom', firstname='Chisom', lastname='Chinweze', email='chisomchisom@gmail.com', gender='Male', avater='img-cat_paint.png')
    user1.hash_password('daniel123')
    user2.hash_password('chisom123')

    book1 = Book(name='Harry Potter', author='J. k. Rowling', edition='4th Edition',
                image='img-0513-2023', description='Story of 3 magicians living their best life in the world', user=user1)
    book2 = Book(name='The Shadow Of What Was Lost', author='James Islington',
                image='img-0505-2024', description='In the world of humans, there live a set of individuals who hold the \
                    ability to control some special powers known only to be held by the gods, they are called the Gifted', user=user2)
    book3 = Book(name='The Echo Of Things To Come', author='James Islington',
                image='img-0503-2025', description='The second book in the Licanous trilogy after "The Shadow of What Was Lost". \
                    It is a continuation of the mysterious happenings in the land of Andara. The three protagonist; Davian, Ash and \
                        Wirr--Torin, continue to work together to bring a solution to what is happening in the North to the boundary \
                            and ensure the safety of the world as we know it.', user=user2)

    review1 = Review(review="One of the best books I've read in a while. I highly recommend to anyone looking for something to relax during the weekend", rating=5, book=book2, user=user1)
    review2 = Review(review="Just when you thought you've had it all in the first book, then this comes. a very good read", rating=4, book=book3, user=user2)
    review3 = Review(review="Such a good book to read. was relaxing for me and I enjoyed all the twist.", rating=3, book=book1, user=user1)
    review4 = Review(review="I don't even know how to express how good this book was, It's just the best!!!", rating=5, book=book2, user=user2)
    review5 = Review(review="The first book I read after a long time of not reading Novels, and I must say, It was really worth it.", rating=4, book=book1, user=user1)
    review6 = Review(review="I was getting sucked in page by page, chapter by chapter. easily my best book for the year!", rating=5, book_id=2, user=user2)

    genre1 = Genre(name='Fiction')
    genre2 = Genre(name='Non Fiction')
    genre3 = Genre(name='Fantasy')

    book1.genre.append(genre1)
    book2.genre.append(genre1)
    book3.genre.append(genre1)

    db.session.add_all([user1, user2])
    db.session.add_all([book1, book2, book3])
    db.session.add_all([review1, review2, review3, review4, review5, review6])
    db.session.add_all([genre1, genre2, genre3])

    db.session.commit()
