#!/usr/bin/env python3
'''Stutus check'''
from flask_restful import Resource
from flask import jsonify, make_response


class Status(Resource):
    '''Check to ensure the API is running'''

    def get(self):
        return make_response({
            'Active': True,
            'message': 'The API is up and running'}, 200)

