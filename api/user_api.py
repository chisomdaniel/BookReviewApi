#!/usr/bin/env python3
'''Manage all the user need'''
from flask_restful import Resource
from flask import jsonify, make_response, request, abort
from models.users import User
from flask_jwt_extended import create_access_token, current_user, jwt_required
from models import db


class Login(Resource):
    '''log a user in'''

    def post(self):
        email = request.form.get('email', None)
        password = request.form.get('password', None)
        user = User.query.filter_by(email=email).one_or_none()
        if not user or user.check_pasword(password):
            return make_response(jsonify({
                'logged_in': False,
                'message': 'Invalid Username or Password'
            }), 401)
        
        assess_token = create_access_token(identity=user)

        return make_response({
            'logged_in': True,
            'access_token': assess_token}, 200)


class Signup(Resource):
    '''add a new user to the database'''

    def post(self):
        username = request.form.get('username', None)
        firstname = request.form.get('firstname', None)
        lastname = request.form.get('lastname', None)
        email = request.form.get('email', None)
        password = request.form.get('password', None)
        gender = request.form.get('gender', None)
        avater = request.form.get('avater', None)

        info_dict = {'username': username,
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'password': password,
        'gender': gender,
        'avater': avater}

        if None in info_dict.keys():
            return make_response(jsonify({
                'status': False,
                'message': 'Incomplete information provided'
            }), 400)
        
        try:
            new_user = User(**info_dict)
            db.session.add(new_user)
            db.session.commit()

            make_response(jsonify({
                'status': True,
                'message': f'Created user {new_user.username} successfully',
            }))
        except Exception as e:
            make_response(jsonify({
                'status': False,
                'message': 'error creating user',
                'error': e
            }))


class User(Resource):
    '''the user api endpoint, for the user profile
    Endpoint =>  /api/me
    '''

    @jwt_required()
    def get(self):
        '''get the info for the current logged in user'''
        return make_response(jsonify(current_user.serialize()), 200)

    @jwt_required()
    def put(self):
        '''Update a user profile'''
        username = request.form.get('username', None)
        firstname = request.form.get('firstname', None)
        lastname = request.form.get('lastname', None)
        password = request.form.get('password', None)
        gender = request.form.get('gender', None)
        avater = request.form.get('avater', None)

        info_dict = {'username': username,
        'firstname': firstname,
        'lastname': lastname,
        'password': password,
        'gender': gender,
        'avater': avater}
        
        try:
            user = current_user
            for i, j in info_dict.keys():
                if j is not None:
                    setattr(user, i, j)
            db.session.commit()
        except Exception as e:
            make_response(jsonify({
                'status': False,
                'message': 'error creating user',
                'error': e
            }))
        
        return make_response(jsonify({
            'status': True,
            'message': f'User {user.username} updated successfully'
        }), 200)


class Users:
    '''Api endpoint to access all users
    Endpoint => /api/users/<int:user_id>'''

    def get(self, user_id=None):
        '''Get a user by id'''

        if user_id == None:
            users = User.query.all()
            user_list = [user.serialize() for user in users]

            return make_response(jsonify(user_list), 200)
        
        user = User.query.get_or_404(user_id, 'No user found with the specified id')
        return make_response(jsonify(user.serialize()), 200)


