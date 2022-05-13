from flask import jsonify #turn things into json responses
from flask import Blueprint

from flask_restful import Resource, Api

import models

class ReviewList(Resource): #resource for a list of courses
    def get(self): #whenever someone sends a get method to the resource
        return jsonify({'reviews': [{'course': 1, 'rating': 5}]})

class Review(Resource):
    def get(self,id): #include id b/c individual courses will always get an id
        return jsonify({'course': 1, 'rating': 5})

    def put(self,id): #include id b/c individual courses will always get an id
        return jsonify({'course': 1, 'rating': 5})

    def delete(self,id): #include id b/c individual courses will always get an id
        return jsonify({'course': 1, 'rating': 5})