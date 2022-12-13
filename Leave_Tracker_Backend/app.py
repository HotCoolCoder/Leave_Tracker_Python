from flask import Flask
from flask import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
STUDENTS = {}
if __name__ == "__main__":
  app.run(debug=True)