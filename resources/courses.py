from flask import jsonify #turn things into json responses

from flask_restful import Resource, Api

import models

class CourseList(Resource): #resource for a list of courses
    def get(self): #whenever someone sends a get method to the resource
        return jsonify({'courses': [{'title': 'Python Basics'}]})

class Course(Resource):
    def get(self,id): #include id b/c individual courses will always get an id
        return jsonify({'title': 'Python Basics'})

    def put(self,id): #include id b/c individual courses will always get an id
        return jsonify({'title': 'Python Basics'})

    def delete(self,id): #include id b/c individual courses will always get an id
        return jsonify({'title': 'Python Basics'})