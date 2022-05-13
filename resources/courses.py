from flask import jsonify #turn things into json responses
from flask import Blueprint

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

courses_api = Blueprint('courses', __name__) #kind of like a module/proxy app w/in an app  
                        # ^path to the file, ^namespace that we're in
api = Api(courses_api) #create an API passingn in the module
api.add_resource(#resource to add
    CourseList, #resource to add
    '/api/v1/courses', #path or uri to give to that resource 
    endpoint='courses' #endpoint to name it... so we can say "I want the courses endpoing"
)

api.add_resource(#resource to add
    Course,
    '/api/v1/course/<int:id>',
    endpoint='course' #you don't have to provide the endpoint name, flask_restful just lowers the name of the resource if not provided
)