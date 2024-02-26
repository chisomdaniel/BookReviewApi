#!/usr/bin/env python3
'''Stutus check'''
from flask_restful import Resource
from flask import jsonify, make_response, request, abort
from models.books import Book
from models.reviews import Review
from models import db
from flask_jwt_extended import current_user, jwt_required


class BooksResource(Resource):
    '''manage the HTTP methods for the book api'''

    def get(self, id=None):
        '''get the info for a particular book
        or all books if `id` is None'''
        if id == None:
            books = Book.query.all()
            book_list = [book.serialize() for book in books]

            return make_response(jsonify(book_list), 200)
        
        book = Book.query.get_or_404(id, 'No book found with the specified id')
        reviews = [f'/api/book/{book.id}/review/{review.id}' for review in book.reviews]
        book_serialized = book.serialize()
        book_serialized.update({'reviews': reviews})
        # add the user that posted it

        return make_response(jsonify(book_serialized), 200)

    @jwt_required()
    def post(self):
        '''Handle the post request for posting/uploading a book with form data'''
        name = request.form.get('name', None)
        author = request.form.get('author', None)
        edition = request.form.get('edition', None)
        image = request.form.get('image', None)  # implement the image upload properly
        description = request.form.get('description', None)
        # add book genre

        if not name:
            return abort(400, 'Book name is required')
        if not author:
            return abort(400, 'Author name is required')
        if not image:
            return abort(400, 'please provide an image of the book')
        if not description:
            return abort(400, 'Description column should not be left empty')
        
        new_book = Book(name=name, author=author, edition=edition, image=image, description=description, user_id=current_user.id)
        db.session.add(new_book)
        db.session.commit()

        return make_response(jsonify({
            'message': 'Book posted successfully',
            'Book name': name,
            'Author': author
        }), 201)

