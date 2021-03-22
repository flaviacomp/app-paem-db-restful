from flask import Flask, request
from flask_restful import Resource, Api

# from sqlalchemy import create_engine
# from json import dumps
# from flask.json import jsonify
# import mysql.connector
# from model.Campus import Campus

# conn = mysql.connector.connect(user='dev', password='Ufop4&2021',
#                               host='127.0.0.1',
#                               database='mydbpaem')

# campus = Campus(conn)

# app = Flask(__name__)
# api = Api(app)

# api.add_resource(campus.get(), '/campus') # Route_1
# app.run(port='5002')

# curl http://127.0.0.1:5000/todo2 -d "data=Do you remember that" -X PUT to do requests in cmd

app = Flask(__name__)
api = Api(app)

todos = dict()

class HelloWorld(Resource):
    def get(self):
        return {"Hello":"World"}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id]= request.form['data']
        return {todo_id: todos[todo_id]}

class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world 1'}

class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world 2'}, 201

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world 3'}, 201, {'Etag': 'some-opaque-string'}

# Adding multiple route
api.add_resource(HelloWorld, '/', '/hello')
# Just one resource for one route
# api.add_resource(Todo1, '/')
# api.add_resource(Todo2, '/')
# api.add_resource(Todo3, '/')

# Adding put and get method
api.add_resource(TodoSimple, '/todo/<string:todo_id>', endpoint="todo_ep")

if __name__=='__main__':
    app.run(debug=True)