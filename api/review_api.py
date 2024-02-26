#!/usr/bin/env python3
'''Stutus check'''
from flask_restful import Resource
from flask import jsonify, make_response, request, abort
from models.books import Book
from models.reviews import Review
from models import db
from flask_jwt_extended import current_user, jwt_required


class ReviewsResource(Resource):
    '''manage the HTTP methods for the review api'''

    def get(self, book_id=None, review_id=None):
        '''get the info for a particular review
        or all reviews under a book given the `book_id`'''

        if book_id == None:
            return make_response(jsonify({
                'book': 'Not found',
                'Description': 'No book ID specified'
            }), 400)
        
        if review_id != None:
            review = Review.query.get_or_404(review_id, 'No review found with the specified id')
            if review.book_id == book_id:
                return make_response(jsonify(review.serialize()), 200)
            else:
                return make_response(jsonify({
                    'message': f'Book ID <{book_id}> under the seclected review ID <{review_id}> do not match'
                }), 400)


        book = Book.query.get_or_404(book_id, '<Review> No Book found with the specified id')
        reviews = book.reviews
        reviews = [review.serialize() for review in reviews]

        return make_response(jsonify(reviews), 200)

    @jwt_required()
    def post(self, book_id=None):
        '''Handle post request with form data'''
        review = request.form.get('review', None)
        rating = request.form.get('rating', None)

        if not book_id:
            return abort(400, 'No Book ID was given')
        if not review:
            return abort(400, 'No Review was given')
        if not rating:
            return abort(400, 'No Rating was provided')
        
        new_review = Review(review=review, rating=rating, book_id=book_id, user_id=current_user.id)
        db.session.add(new_review)
        db.session.commit()

        return make_response(jsonify({
            'message': 'Review posted successfully',
            'review': review,
            'rating': rating
        }), 201)
    
    @jwt_required()
    def put(self):
        '''api endpoint for a user to update their review'''

    @jwt_required()
    def delete(self):
        '''api endpoint for a user to delete their review'''

