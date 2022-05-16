from dataclasses import fields
from flask import jsonify, url_for #turn things into json responses
from flask import Blueprint, abort

from flask_restful import (Resource, Api, reqparse ,marshal,
                        marshal_with, inputs, fields, url_for)

import models 

review_fields = {
    'id': fields.Integer,
    'for_course': fields.String,
    'rating': fields.Integer,
    'comment': fields.String(default=''),
    'created_at': fields.DateTime
}

def review_or_404(review_id):
    try:
        review = models.Review.get(models.Review.id == review_id)
    except models.Review.DoesNotExist:
        abort(404)
    else:
        return review

def add_course(review):
    review.for_course = url_for('resources.course.course', id=review.course.id)
    return review


class ReviewList(Resource): #resource for a list of courses
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
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
            default=''
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