import flask
#from flask_cors import CORS
import json
import os
#import tensorflow

# Initializing flask app
app = flask.Flask(__name__)

# Adding cors to flask
#CORS(app)

# Controller-1
@app.route("/", methods=['GET'])
def hello_world():
    return 'Hello, !'


# Running the api
if __name__ == '__main__':
     app.run(debug=True)
