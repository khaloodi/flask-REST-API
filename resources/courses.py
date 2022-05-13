from flask import jsonify #turn things into json responses
from flask import Blueprint

from flask_restful import Resource, Api, reqparse, inputs

import models

class CourseList(Resource): #resource for a list of courses
    #add parser
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument( #add arguments for each of the things or fields that we want to have come in
            'title',
            required=True,
            help='No course title provided',
            location=['form','json'] #telling reqparser where to look for this data.. here we're saying look in form input data
            #look in ^form encoded or json data (json usually stored in the body of the request)
            #whichever comes last in the list is the first one that reqparser tries or looks in
        )
        self.reqparse.add_argument(
            'url',
            required=True,
            help='No course URL provided',
            location= ['form', 'json'],
            type=inputs.url
        )
        super().__init__()

    def get(self): #whenever someone sends a get method to the resource
        return jsonify({'courses': [{'title': 'Python Basics'}]})

    def post(self):
        args = self.reqparse.parse_args()
        #save the model instance after saving the args; args becomes a dictionary off all the post items
        models.Course.create(**args) #take the args dictionary, feed all that into Course.create
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