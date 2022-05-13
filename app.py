from flask import Flask 

import models
from resources.courses import courses_api
from resources.reviews import reviews_api

DEBUG = True
HOST = '0.0.0.0'
PORT = 8000

app = Flask(__name__) #flask pays attention to current file
app.register_blueprint(courses_api)
app.register_blueprint(reviews_api, url_prefix='/api/v1/') #different way to write uri prefix

@app.route('/')
def index():
    return 'hi'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)