from flask import jsonify #turn things into json responses
from flask import Blueprint

from flask_restful import Resource, Api, reqparse, inputs

import models

class ReviewList(Resource): #resource for a list of courses
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqpars.add_argument(
            'course',
            type=inputs.positive,
            required=True,
            help='No course provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'rating',
            type=inputs.int_range(1,5),
            required=True,
            help='No rating provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'comment',
            required=False,
            nullable=True,
            location=['form', 'json'],
            defaul=''
        )
        super().__init__()

    def get(self): #whenever someone sends a get method to the resource
        return jsonify({'reviews': [{'course': 1, 'rating': 5}]})

class Review(Resource):
    def get(self,id): #include id b/c individual courses will always get an id
        return jsonify({'course': 1, 'rating': 5})

    def put(self,id): #include id b/c individual courses will always get an id
        return jsonify({'course': 1, 'rating': 5})

    def delete(self,id): #include id b/c individual courses will always get an id
        return jsonify({'course': 1, 'rating': 5})

reviews_api = Blueprint('reviews', __name__)
api = Api(reviews_api)
api.add_resource(
    ReviewList,
    '/reviews',
    endpoint='reviews'
)

api.add_resource(
    Review,
    '/reviews/<int:id>',
    endpoint='review'
)