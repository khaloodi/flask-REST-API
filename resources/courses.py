from flask import jsonify #turn things into json responses
from flask import Blueprint, url_for, abort

from flask_restful import (Resource, Api, reqparse ,marshal,
                        marshal_with, inputs, fields, url_for)

import models

#all the fields that describe a course, returned by api:
course_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'url': fields.String, #note, fields.Url is used to point to another record w/in the Api, this is why we use fields.String
    'reviews': fields.List(fields.String)
}

def add_reviews(course):
        course.reviews = [url_for('resources.reviews.review', id=review.id) for reveiw in course.review_set]
        return course

def course_or_404(course_id):
    try:
        course = models.Course.get(models.Course.id == course_id)
    except models.Course.DoesNotExist:
        abort(404)
    else:
        return course

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
        # to handle the following: TypeError: Object of type ModelSelect is not JSON serializable
        # flask uses marshal:  ... [marshal() for item in select statement]
        # provide marshal with record or records and the fields defined for that resource
        courses = [marshal(add_reviews(course), course_fields) for course in models.Course.select()] #get all the courses
        # return jsonify({'courses': [{'title': 'Python Basics'}]})
        return jsonify({'courses': courses})

    @marshal_with(course_fields)
    def post(self):
        args = self.reqparse.parse_args()
        #save the model instance after saving the args; args becomes a dictionary off all the post items
        course = models.Course.create(**args) #take the args dictionary, feed all that into Course.create
        # return jsonify({'courses': [{'title': 'Python Basics'}]})
        return (add_reviews(course), 201, {
            'Location': url_for('resources.courses.course', id=course.id)
        })


class Course(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            required=True,
            help='No course title provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'url',
            required=True,
            help='No course URL provided',
            location=['form', 'json'],
            type=inputs.url
        )
        super().__init__()

    @marshal_with(course_fields) #marshal_with decorator useful for when working with one specific thing
    def get(self, id): #include id b/c individual courses will always get an id
        # return jsonify({'title': 'Python Basics'})
        return add_reviews(course_or_404(id))

    @marshal_with(course_fields)
    def put(self,id): #include id b/c individual courses will always get an id
        args = self.reqparse.parse_args()
        query = models.Course.update(**args).where(models.Course.id==id)
        query.execute()
        # return jsonify({'title': 'Python Basics'})
        return (add_reviews(models.Course.get(models.Course.id==id)),200, #put request is returning JSON data for now, as well as a 200 status code
                {'Location': url_for('resources.courses.course', id=id)}) #responding w/a location header that says where the data was posted

    def delete(self,id): #include id b/c individual courses will always get an id
        # return jsonify({'title': 'Python Basics'})
        query = models.Course.delete().where(models.Course.id==id)
        query.execute()
        # return jsonify({'title': 'Python Basics'})
        return ('',204, #responding w/an empty body and 204
                {'Location': url_for('resources.courses.courses')}) #sending back location header to courses not course to send user to where other stuff is

courses_api = Blueprint('courses', __name__) #kind of like a module/proxy app w/in an app  
                        # ^path to the file, ^namespace that we're in
api = Api(courses_api) #create an API passingn in the module
api.add_resource(#resource to add
    CourseList, #resource
    '/api/v1/courses', #path or uri to give to that resource 
    endpoint='courses' #endpoint to name it... so we can say "I want the courses endpoing"
)

api.add_resource(#resource to add
    Course, #resource
    '/api/v1/courses/<int:id>',
    endpoint='course' #you don't have to provide the endpoint name, flask_restful just lowers the name of the resource if not provided
)